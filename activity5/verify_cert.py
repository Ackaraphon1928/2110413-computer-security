from OpenSSL import crypto
import pem


def load_pem_file(filename):
    with open(filename, "rb") as f:
        return f.read()


def verify_chain_of_trust(
    target_cert_file,
    intermediate_cert_file,
    ca_bundle_file
):
    # Load server/leaf certificate
    target_pem = load_pem_file(target_cert_file)

    target_cert = crypto.load_certificate(
        crypto.FILETYPE_PEM,
        target_pem
    )

    # Load intermediate certificate
    intermediate_pem = load_pem_file(intermediate_cert_file)

    intermediate_cert = crypto.load_certificate(
        crypto.FILETYPE_PEM,
        intermediate_pem
    )

    # Create trust store
    store = crypto.X509Store()

    # Add root CA certificates
    root_pems = pem.parse_file(ca_bundle_file)

    for root_pem in root_pems:
        try:
            root_cert = crypto.load_certificate(
                crypto.FILETYPE_PEM,
                root_pem.as_bytes()
            )
            store.add_cert(root_cert)

        except Exception:
            # Ignore duplicates or incompatible entries
            pass

    try:
        # Intermediate is supplied as an untrusted chain certificate.
        store_ctx = crypto.X509StoreContext(
            store,
            target_cert,
            [intermediate_cert]
        )

        store_ctx.verify_certificate()

        print("Certificate verified")
        return True

    except crypto.X509StoreContextError as e:
        print("Certificate verification failed")
        print(e)
        return False


if __name__ == "__main__":
    verify_chain_of_trust(
        "target.cert",
        "intermediate.cert",
        "ca-certificates.crt"
    )