# %% [markdown]
# # 🚀 MISSION 1: THE GAME WALKER
# ### "Moving Without Loops"
# 
# **TUJUAN:** Membuktikan bahwa pergerakan karakter dalam game hanyalah operasi penjumlahan vektor. Anda akan memindahkan karakter dari titik nol ke tujuan akhir tanpa mengubah koordinat x dan y secara manual satu per satu.
# 
# ---
# 
# ### 🧠 KONSEP MATEMATIKA
# Posisi adalah Vektor. Gerakan adalah Vektor.
# Posisi baru adalah hasil penjumlahan posisi lama dengan vektor langkah.
# 
# $$\vec{P}_{akhir} = \vec{P}_{awal} + \vec{v}_1 + \vec{v}_2 + \dots + \vec{v}_n$$
# 
# Atau dalam bahasa NumPy (Vectorization):
# $$\vec{P}_{akhir} = \sum (\text{semua vektor gerakan})$$
# 
# ---
# 
# ### 📝 INSTRUKSI TUGAS
# 
# 1.  **Definisi Gerakan (Kamus Vektor):**
#     * Buat vektor dasar menggunakan NumPy:
#         * `UP` = `[0, 5]`
#         * `DOWN` = `[0, -5]`
#         * `RIGHT` = `[5, 0]`
#         * `LEFT` = `[-5, 0]`
# 
# 2.  **Skenario Perjalanan:**
#     * Buat sebuah list berisi urutan langkah acak, misal: `[UP, RIGHT, UP, LEFT, UP, DOWN, RIGHT]`.
# 
# 3.  **Kalkulasi Posisi:**
#     * Gunakan `np.sum(..., axis=0)` untuk mencari koordinat akhir secara instan.
#     * *(Advanced)*: Gunakan `np.cumsum(..., axis=0)` jika ingin mendapatkan seluruh jejak koordinat (trail).
# 
# 4.  **Visualisasi:**
#     * Gunakan fungsi `plot_vectors` (yang sudah Anda buat sebelumnya) untuk menggambar perjalanan karakter tersebut dari (0,0) hingga titik akhir.
# 
# > **Filosofi:** Jangan berpikir "X tambah 1". Berpikirlah "Tambahkan Vektor Kanan".

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
def vec_addition(vectors: list[np.ndarray], colors: list[str]) -> None:
    """
    visualizes vector addition using head-to-tail method and plots the resultant vector

    Args:
        vectors (list[np.ndarray]): list of 2D NumPy arrays representing the vectors
        colors (list[str]): list of color strings for each vector path
    """
    plt.style.use("dark_background")
    plt.figure(figsize=(8,8))
    plt.axvline(color="grey", lw=1)
    plt.axhline(color="grey", lw=1)
    
    origin = np.array([0,0])
    start = origin.copy()
    
    for i, vec in enumerate(vectors):
        color = colors[i] if i < len(colors) else "white"
        
        plt.quiver(
            *start, *vec,
            angles='xy', scale_units='xy', scale=1,
            color=color, label=f"v-{i+1}",
            zorder=2.1
            )
        start += vec
    
    final = np.sum(vectors, axis=0)
    plt.quiver(
        *origin, *final,
        angles='xy', scale_units='xy', scale=1,
        color="purple", label=f"resultant ({final[0]},{final[1]})",
        zorder=5
        )
    
    plt.grid(linestyle='--', alpha=0.3)
    
    limit = np.max(np.abs(np.cumsum(vectors, axis=0))) + 3
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    plt.legend(fontsize='x-small')
    plt.title("Vector Addition")
    
    plt.show()

# %%
def visualize(vectors: list[np.ndarray], colors: list[str]) -> None:
    """
    visualizes vector

    Args:
        vectors (list[np.ndarray]): list of 2D NumPy arrays representing the vectors
        colors (list[str]): list of color strings for each vector path
    """
    plt.style.use("dark_background")
    plt.figure(figsize=(8,8))
    plt.axvline(color="grey", lw=1)
    plt.axhline(color="grey", lw=1)
    
    origin = np.array([0,0])
    
    for i, vec in enumerate(vectors):
        color = colors[i] if i < len(colors) else "white"
        
        plt.quiver(
            *origin, *vec,
            angles='xy', scale_units='xy', scale=1,
            color=color, label=f"v-{i+1}",
            zorder=2.1
            )
    
    plt.grid(linestyle='--', alpha=0.3)
    
    limit = np.max(np.abs(np.cumsum(vectors, axis=0))) + 5
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    plt.legend(fontsize='x-small')
    plt.title("Rotated Vector")
    
    plt.show()

# %%
a = np.array([3, 5])
b = np.array([-7, 4])

# %%
vec_addition([a, b], ["red", "green"])

# %%
up = np.array([0,5])
down = np.array([0,-5])
right = np.array([5,0])
left = np.array([-5,0])

c_up = "red"
c_down = "green"
c_right = "blue"
c_left = "yellow"

gerak = [up, right, down, down, left, left, left, up, left, up]
colors = [c_up, c_right, c_down, c_down, c_left, c_left, c_left, c_up]

vec_addition(gerak, colors)


