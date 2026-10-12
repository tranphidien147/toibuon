import cv2

def rotate_frame(frame, angle):
    """
    Hàm xoay khung hình theo góc: 0, 90, 180, 270 độ
    """
    angle = angle % 360
    if angle == 90:
        return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)          # Xoay 90 độ cùng chiều KĐH
    elif angle == 180:
        return cv2.rotate(frame, cv2.ROTATE_180)                   # Xoay 180 độ
    elif angle == 270:
        return cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)   # Xoay 270 độ (tức 90 độ ngược chiều KĐH)
    return frame  # 0 độ: giữ nguyên khung hình ban đầu

def main():
    # Thay 'vdtest.mp4' bằng đường dẫn đến file video của bạn
    video_path = "vdtest.mp4"

    # Mở video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Lỗi: Không thể mở video tại '{video_path}'. Vui lòng kiểm tra lại đường dẫn!")
        return

    # Lấy FPS của video để phát đúng tốc độ thực tế
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps) if fps > 0 else 30

    current_angle = 0  # Góc xoay ban đầu

    print("=== HƯỚNG DẪN ĐIỀU KHIỂN ===")
    print(" - Nhấn 'A' / 'a': Xoay ngược chiều kim đồng hồ 90 độ")
    print(" - Nhấn 'D' / 'd': Xoay theo chiều kim đồng hồ 90 độ")
    print(" - Nhấn 'Q' / ESC: Thoát chương trình")
    print("===========================")

    while True:
        ret, frame = cap.read()

        # Dừng khi hết video
        if not ret:
            print("Đã phát hết video.")
            break

        # Xoay khung hình theo góc hiện tại
        rotated_frame = rotate_frame(frame, current_angle)

        # Hiển thị thông số góc xoay lên khung hình
        info_text = f"Goc xoay: {current_angle} do (A: Nghich, D: Thuan)"
        cv2.putText(
            rotated_frame,
            info_text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

        # Hiển thị video lên cửa sổ
        cv2.imshow("Video Player", rotated_frame)

        # Đọc phím bấm
        key = cv2.waitKey(delay) & 0xFF

        # Phím 'A' hoặc 'a': Xoay ngược chiều kim đồng hồ (-90 độ)
        if key == ord('a') or key == ord('A'):
            current_angle = (current_angle - 90) % 360
            print(f">> Nhấn A: Xoay ngược chiều KĐH -> Góc hiện tại: {current_angle}°")

        # Phím 'D' hoặc 'd': Xoay cùng chiều kim đồng hồ (+90 độ)
        elif key == ord('d') or key == ord('D'):
            current_angle = (current_angle + 90) % 360
            print(f">> Nhấn D: Xoay cùng chiều KĐH -> Góc hiện tại: {current_angle}°")

        # Phím 'Q' hoặc phím ESC (mã 27): Thoát
        elif key == ord('q') or key == ord('Q') or key == 27:
            print("Thoát chương trình.")
            break

    # Giải phóng bộ nhớ và đóng cửa sổ
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()