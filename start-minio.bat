@echo off
echo Starting MinIO server...
echo.
echo MinIO will be available at:
echo API: http://localhost:9000
echo Console: http://localhost:9001
echo.
echo Default credentials: minioadmin/minioadmin
echo.
docker run -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ":9001"