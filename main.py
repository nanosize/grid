import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def draw_grid_and_x(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path)
    if image is None:
        messagebox.showerror("エラー", "画像を読み込めませんでした。ファイルパスを確認してください。")
        return
    
    # 画像の高さと幅を取得
    height, width, _ = image.shape

    # 線の設定
    line_color = (0, 255, 0)  # 緑
    line_thickness = 2       # 線の太さを2ピクセルに設定

    # 格子を描画
    cell_width = width // 3
    cell_height = height // 3
    for i in range(1, 3):  # 縦線
        x = i * cell_width
        cv2.line(image, (x, 0), (x, height), line_color, line_thickness)
    for j in range(1, 3):  # 横線
        y = j * cell_height
        cv2.line(image, (0, y), (width, y), line_color, line_thickness)

    # 全体に「ばってん」を描画
    cv2.line(image, (0, 0), (width, height), line_color, line_thickness)  # 対角線1
    cv2.line(image, (0, height), (width, 0), line_color, line_thickness)  # 対角線2

    # 出力先の画像の名前を設定
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    output_path = os.path.join(os.path.dirname(image_path), f"{name}_grid{ext}")

    # 結果を保存
    cv2.imwrite(output_path, image)
    messagebox.showinfo("成功", f"結果の画像を {output_path} に保存しました。")

def select_image():
    image_path = filedialog.askopenfilename(title="画像を選択", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if image_path:
        draw_grid_and_x(image_path)  # URLエンコードを削除

# GUIの設定
root = tk.Tk()
root.title("グリッドばってん描画ツール")
root.geometry("300x150")

select_button = tk.Button(root, text="画像を選択してグリッドを描画", command=select_image)
select_button.pack(pady=50)

root.mainloop()
