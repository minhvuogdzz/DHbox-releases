# DHbox releases

Bản phát hành của **DHbox**, app macOS trên thanh menu của Devhouse Software. Repo này chỉ chứa bản phát hành; mã nguồn nằm ở repo riêng.

## Cài đặt

Cách nhanh nhất, không bị macOS chặn lần mở đầu: mở Terminal, dán rồi bấm Return.

```bash
curl -fsSL https://github.com/minhvuogdzz/DHbox-releases/releases/latest/download/install.sh | sh
```

Hoặc cài bằng DMG:

1. Tải `DHbox-<phiên bản>.dmg` ở mục [Releases](../../releases/latest) và mở nó.
2. Kéo `DHbox.app` vào lối tắt Applications trong cửa sổ vừa hiện.
3. Bản được ký riêng, chưa notarize, nên macOS có thể chặn lần mở đầu. Vào Cài đặt hệ thống, Quyền riêng tư và Bảo mật, kéo xuống mục Bảo mật, bấm "Vẫn mở" cạnh DHbox. (Từ macOS 15, bấm chuột phải rồi chọn Mở không còn qua được.) Hoặc chạy `xattr -cr /Applications/DHbox.app` trong Terminal.

Sau đó DHbox tự kiểm tra bản mới mỗi ngày. Trong Cài đặt có thể bật tự động tải và cài; mọi bản tải về đều được kiểm tra chữ ký Ed25519 (`DHbox-<phiên bản>.zip.sig`; bộ cập nhật trong app dùng tệp `.zip`, còn `.dmg` dành cho cài lần đầu) trước khi cài.

## Phát hành bản mới (dành cho người bảo trì)

1. Đổi `MARKETING_VERSION` trong `project.yml` của mã nguồn, commit, rồi gắn tag `vX.Y.Z` và đẩy lên.
2. Tạo release ở repo này với đúng tag `vX.Y.Z`, đánh dấu pre-release. Workflow `Build and publish` sẽ build, ký, đính kèm tệp rồi chuyển thành bản mới nhất.
