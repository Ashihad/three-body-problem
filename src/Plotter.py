import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ThreeBodyPlotter:
  def __init__(self, solution):
    self.solution = solution

  def plot(self):
    """
    Plot the solutions for all 6 variables.
    
    Parameters:
    solution (OdeResult): Solution from solve_ivp
    """
    plt.figure(figsize=(15, 10))
    
    x1, y1 = self.solution.y[0], self.solution.y[1]
    x2, y2 = self.solution.y[2], self.solution.y[3]
    x3, y3 = self.solution.y[4], self.solution.y[5]

    # Position components
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, label='Body 1', color='red')
    plt.plot(x2, y2, label='Body 2', color='blue')
    plt.plot(x3, y3, label='Body 3', color='green')
    plt.title('Three-Body Problem Trajectory')
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

  def make_gif(self):
    # Interpolate solution to get smooth animation
    num_frames = 500
    t = np.linspace(self.solution.t[0], self.solution.t[-1], num_frames)
    sol = self.solution.sol(t)
    
    # Prepare the figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title('Three-Body Problem Simulation')
    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    
    # Compute max position for axis limits
    max_pos = np.max(np.abs(sol[:6]))
    ax.set_xlim(-max_pos*1.2, max_pos*1.2)
    ax.set_ylim(-max_pos*1.2, max_pos*1.2)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # Initialize plot objects
    line1, = ax.plot([], [], 'r-', alpha=0.3, linewidth=1, label='Body 1')
    line2, = ax.plot([], [], 'b-', alpha=0.3, linewidth=1, label='Body 2')
    line3, = ax.plot([], [], 'g-', alpha=0.3, linewidth=1, label='Body 3')
    
    point1, = ax.plot([], [], 'ro', markersize=10)
    point2, = ax.plot([], [], 'bo', markersize=8)
    point3, = ax.plot([], [], 'go', markersize=6)
    
    # Traces for trajectories
    trace_length = min(100, num_frames)
    traces = [[], [], []]
    
    def init():
        """Initialize the animation."""
        traces[0].clear()
        traces[1].clear()
        traces[2].clear()

        line1.set_data([], [])
        line2.set_data([], [])
        line3.set_data([], [])
        point1.set_data([], [])
        point2.set_data([], [])
        point3.set_data([], [])
        return line1, line2, line3, point1, point2, point3
    
    def animate(frame_num):
        """Animation update function."""
        # Current positions
        x1, y1 = sol[0, frame_num], sol[1, frame_num]
        x2, y2 = sol[2, frame_num], sol[3, frame_num]
        x3, y3 = sol[4, frame_num], sol[5, frame_num]
        
        if frame_num == 0:
          traces[0].clear()
          traces[1].clear()
          traces[2].clear()

        # Update traces
        traces[0].append((x1, y1))
        traces[1].append((x2, y2))
        traces[2].append((x3, y3))
        
        # Limit trace length
        traces[0] = traces[0][-trace_length:]
        traces[1] = traces[1][-trace_length:]
        traces[2] = traces[2][-trace_length:]
        
        # Unpack traces
        x1_trace = [p[0] for p in traces[0]]
        y1_trace = [p[1] for p in traces[0]]
        x2_trace = [p[0] for p in traces[1]]
        y2_trace = [p[1] for p in traces[1]]
        x3_trace = [p[0] for p in traces[2]]
        y3_trace = [p[1] for p in traces[2]]
        
        # Update lines and points
        line1.set_data(x1_trace, y1_trace)
        line2.set_data(x2_trace, y2_trace)
        line3.set_data(x3_trace, y3_trace)
        
        # Ensure data is a list/array for set_data
        point1.set_data([x1], [y1])
        point2.set_data([x2], [y2])
        point3.set_data([x3], [y3])
        
        return line1, line2, line3, point1, point2, point3
    
    # Create animation
    anim = animation.FuncAnimation(
        fig, 
        animate, 
        init_func=init,
        frames=num_frames, 
        interval=20,  # 20 ms between frames
        blit=True
    )
    
    plt.legend()
    plt.tight_layout()
    
    # Save animation 
    try:
        print("Saving gif...")
        anim.save('three_body_simulation.gif', writer='pillow')
        print("Animation saved as three_body_simulation.gif")
    except Exception as e:
        print(f"Could not save animation: {e}")
    
    plt.show()