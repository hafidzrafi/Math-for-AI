import numpy as np
import matplotlib.pyplot as plt

def vecs_visualize(vectors: list[np.ndarray], colors: list[str]) -> None:
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
    plt.title("Vector")
    
    plt.show()

def vecs_addition(vectors: list[np.ndarray], colors: list[str]) -> None:
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
    
def vecs_visualize_3d(vectors, colors, labels):
    """
    Memvisualisasikan list vektor 3D ke dalam ruang Cartesian 3D.
    """
    fig = plt.figure(figsize=(8, 8))
    # INI KUNCINYA: Projection '3d'
    ax = fig.add_subplot(111, projection='3d')

    # Origin selalu (0,0,0)
    origin = np.array([0, 0, 0])

    for i, vec in enumerate(vectors):
        # Quiver 3D butuh 6 argumen: x, y, z (asal), u, v, w (arah)
        ax.quiver(
            origin[0], origin[1], origin[2], # Titik Asal
            vec[0], vec[1], vec[2],          # Arah Vector
            color=colors[i], 
            label=labels[i],
            arrow_length_ratio=0.1,          # Agar panah tidak terlalu gemuk
            linewidth=2
        )

    # Setting Limit agar visualisasi tidak "zoom in" terlalu dekat
    limit = np.max(np.abs(vectors)) + 2
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_zlim([-limit, limit])

    # Label Sumbu (Penting di 3D biar tidak tersesat)
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    
    # Menambah garis bantu sumbu
    ax.plot([-limit, limit], [0, 0], [0, 0], 'k--', alpha=0.2) # Sumbu X
    ax.plot([0, 0], [-limit, limit], [0, 0], 'k--', alpha=0.2) # Sumbu Y
    ax.plot([0, 0], [0, 0], [-limit, limit], 'k--', alpha=0.2) # Sumbu Z

    plt.title("Vector 3d")
    plt.legend()
    plt.show()

def show_image(img):
    plt.figure(figsize=(4,4))
    plt.imshow(img)
    plt.show()
    