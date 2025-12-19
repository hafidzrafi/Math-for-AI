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
    plt.title("Rotated Vector")
    
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

def show_image(img):
    plt.figure(figsize=(4,4))
    plt.imshow(img)
    plt.show()
    