import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def merge_sort_visualize(arr):
    """
    Perform Merge Sort on 'arr' and yield (list_of_values, indices_being_compared) 
    at each important step for visualization.
    """
    # This list will be used to store snapshots of our list at various stages
    # along with the indices being merged or compared.
    
    # A helper function to do the merging of two sorted sublists
    def merge(left, right, start):
        i, j = 0, 0
        merged = []
        
        while i < len(left) and j < len(right):
            # We yield the current array + the indices being compared
            # left_part starts from 'start' and goes up to 'start + len(left)-1'
            # right_part starts from 'start + len(left)' onwards
            yield arr, (start + i, start + len(left) + j)
            
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                
        # Copy any remaining elements
        while i < len(left):
            yield arr, (start + i, start + i)  # Not a real comparison, but for coloring
            merged.append(left[i])
            i += 1
            
        while j < len(right):
            yield arr, (start + len(left) + j, start + len(left) + j)
            merged.append(right[j])
            j += 1
            
        # Place the merged array back into the main list
        for idx, val in enumerate(merged):
            arr[start + idx] = val
            # Yield after placing each element
            yield arr, (start + idx, start + idx)
    
    def merge_sort(start, end):
        # If the segment is more than one element, split and merge
        if end - start > 1:
            mid = (start + end) // 2
            yield from merge_sort(start, mid)
            yield from merge_sort(mid, end)
            yield from merge(arr[start:mid], arr[mid:end], start)

    yield from merge_sort(0, len(arr))

# ---------------------------------------------------------
# Below is the code that sets up the visualization with matplotlib
# ---------------------------------------------------------

def visualize_merge_sort():
    # Generate a random list
    n = 20
    arr = [i+1 for i in range(n)]
    random.shuffle(arr)
    
    # Create a generator that yields snapshots (array states + indices)
    generator = merge_sort_visualize(arr)

    fig, ax = plt.subplots()
    ax.set_title("Merge Sort Visualization")
    
    # Initial bar container
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    
    # Text label for the iteration
    iteration_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    
    # We will color bars differently to highlight comparisons
    def update(frame):
        array_data, (idx1, idx2) = frame
        
        # Update the heights of the bars
        for rect, val in zip(bar_rects, array_data):
            rect.set_height(val)
            rect.set_color("blue")
        
        # Highlight the bars being compared or merged
        bar_rects[idx1].set_color("red")
        bar_rects[idx2].set_color("yellow")
        
        iteration_text.set_text(f"Comparing indices: {idx1} and {idx2}")

    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=generator, 
        interval=500,  # Time in ms between frames
        repeat=False,
        blit=False,
        cache_frame_data=False
    )
    
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()
    
    return ani

if __name__ == "__main__":
    anim = visualize_merge_sort()
