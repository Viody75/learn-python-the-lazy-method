# from couchbase.cluster import Cluster, ClusterOptions
# from couchbase.auth import PasswordAuthenticator
# from couchbase.collection import UpsertOptions
# from couchbase.exceptions import CouchbaseException
# import json

# # RUN
# #
# #
# #

# # Konfigurasi koneksi Couchbase
# COUCHBASE_HOST = "couchbase://127.0.0.1"  # ganti dengan IP VPS jika remote
# USERNAME = "Administrator"                 # ganti sesuai login admin Couchbase kamu
# PASSWORD = "password123"                   # ganti dengan password kamu
# BUCKET_NAME = "test_bucket"                # bucket tempat penyimpanan data

# def main():
#     try:
#         # Koneksi ke cluster Couchbase
#         cluster = Cluster(
#             COUCHBASE_HOST,
#             ClusterOptions(PasswordAuthenticator(USERNAME, PASSWORD))
#         )

#         # Pastikan koneksi siap
#         cluster.wait_until_ready(10)
#         print("✅ Connected to Couchbase cluster.")

#         # Ambil bucket dan koleksi default
#         bucket = cluster.bucket(BUCKET_NAME)
#         collection = bucket.default_collection()

#         # Data yang akan di-seed
#         doc_id = "user_001"
#         doc_data = {
#             "name": "Viody",
#             "email": "viody@example.com",
#             "role": "admin"
#         }

#         # Upsert data (insert or replace)
#         result = collection.upsert(doc_id, doc_data, UpsertOptions(timeout=5))
#         print(f"✅ Data inserted/updated successfully: {result}")

#         # Verifikasi (baca data kembali)
#         get_result = collection.get(doc_id)
#         print("📄 Retrieved document:")
#         print(json.dumps(get_result.content_as[dict], indent=2))

#     except CouchbaseException as e:
#         print(f"❌ Couchbase error: {e}")
#     except Exception as ex:
#         print(f"⚠️ Unexpected error: {ex}")

# if __name__ == "__main__":
#     main()
