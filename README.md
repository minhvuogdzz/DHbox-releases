# DHbox releases

Bản phát hành của **DHbox**, app macOS trên thanh menu của Devhouse Software. Repo này chỉ chứa bản phát hành; mã nguồn nằm ở repo riêng.

## Cài đặt

1. Tải `DHbox-<phiên bản>.zip` ở mục [Releases](../../releases/latest).
2. Giải nén và kéo `DHbox.app` vào thư mục Applications.
3. Bản được ký thường (chưa notarize): lần đầu mở, bấm chuột phải vào app, chọn Mở, rồi xác nhận.

Sau đó DHbox tự kiểm tra bản mới mỗi ngày. Trong Cài đặt có thể bật tự động tải và cài; mọi bản tải về đều được kiểm tra chữ ký Ed25519 (`DHbox-<phiên bản>.zip.sig`) trước khi cài.

## Phát hành bản mới (dành cho người bảo trì)

1. Đổi `MARKETING_VERSION` trong `project.yml` của mã nguồn, commit, rồi gắn tag `vX.Y.Z` và đẩy lên.
2. Tạo release ở repo này với đúng tag `vX.Y.Z`, đánh dấu pre-release. Workflow `Build and publish` sẽ build, ký, đính kèm tệp rồi chuyển thành bản mới nhất.
