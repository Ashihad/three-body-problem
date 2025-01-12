import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import logging

class ThreeBodyPlotter:
  def __init__(self, solution, params):
    self.solution = solution
    self.params = params
    self.logger = logging.getLogger('main')
    self.detailed_path = params['detailed_file']
    self.phase_path = params['phase_file']
    self.animation_path = params['animation_file']
    self.quiet = params['quiet']

  def plot_detailed(self, resolution=500):
    """
    Plot the solutions for all 6 variables.
    """

    x1, y1 = self.solution.y[0], self.solution.y[1]
    x2, y2 = self.solution.y[2], self.solution.y[3]
    x3, y3 = self.solution.y[4], self.solution.y[5]
    vx1, vy1 = self.solution.y[6], self.solution.y[7]
    vx2, vy2 = self.solution.y[8], self.solution.y[9]
    vx3, vy3 = self.solution.y[10], self.solution.y[11]

    t = np.linspace(self.solution.t[0], self.solution.t[-1], len(x1))

    # Position components
    fig, axes = plt.subplots(3, 2)
    fig.set_size_inches((15, 10))
    if self.params['title']:
      fig.suptitle(self.params['title'])

    # setup basic properties for r plots
    for i, j in zip((0,1,2), (0,0,0)):
      axes[i][j].set_xlabel("t [s]")
      axes[i][j].set_ylabel("r [m]")
      axes[i][j].grid(True)
    axes[0][0].plot(t, np.sqrt(x1**2 + y1**2), label='r(Body 1)', color='red')
    axes[1][0].plot(t, np.sqrt(x2**2 + y2**2), label='r(Body 2)', color='green')
    axes[2][0].plot(t, np.sqrt(x3**2 + y3**2), label='r(Body 3)', color='blue')

    # setup basic properties for v plots
    for i, j in zip((0,1,2), (1,1,1)):
      axes[i][j].set_xlabel("t [s]")
      axes[i][j].set_ylabel("v [m/s]")
      axes[i][j].grid(True)
    axes[0][1].plot(t, np.sqrt(vx1**2 + vy1**2), label='v(Body 1)', color='red')
    axes[1][1].plot(t, np.sqrt(vx2**2 + vy2**2), label='v(Body 2)', color='green')
    axes[2][1].plot(t, np.sqrt(vx3**2 + vy3**2), label='v(Body 3)', color='blue')

    fig.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    fig.tight_layout()
    plt.savefig(self.detailed_path)
    if not self.quiet:
      plt.show()

  def plot_phase(self):
    fig, ax = plt.subplots()
    fig.set_size_inches((10, 10))
    
    x1, y1 = self.solution.y[0], self.solution.y[1]
    x2, y2 = self.solution.y[2], self.solution.y[3]
    x3, y3 = self.solution.y[4], self.solution.y[5]

    # Position components
    ax.plot(x1, y1, label='Body 1', color='red')
    ax.plot(x2, y2, label='Body 2', color='green')
    ax.plot(x3, y3, label='Body 3', color='blue')
    if self.params['title']:
      ax.set_title(self.params['title'])
    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True)
    
    ax.set_aspect('equal', 'box')
    fig.tight_layout()
    plt.savefig(self.phase_path)
    if not self.quiet:
      plt.show()

  def make_gif(self, num_frames=500):
    # Interpolate solution to get smooth animation
    t = np.linspace(self.solution.t[0], self.solution.t[-1], num_frames)
    sol = self.solution.sol(t)
    
    # Prepare the figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
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
    point2, = ax.plot([], [], 'bo', markersize=10)
    point3, = ax.plot([], [], 'go', markersize=10)
    
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
    self.logger.info("Generating animation...")
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
    self.logger.info("Animation generated...")

    # Save animation 
    try:
      self.logger.info("Saving animation...")
      anim.save(self.animation_path, writer='pillow')
      self.logger.info(f"Animation saved as \"{self.animation_path}\"")
    except Exception as e:
      self.logger.critical(f"Could not save animation: {e}")
    
    if not self.quiet:
      plt.show()
