import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display

# 1. Projectile Motion Equations (Calculus-based)
def calculate_trajectory(v0, theta, g=9.81):
    """
    වස්තුවේ ගමන් පථය ගණනය කරයි / Calculates the projectile trajectory
    v0: ආරම්භක ප්‍රවේගය (Initial velocity in m/s)
    theta: ආරම්භක කෝණය (Launch angle in degrees)
    g: ගුරුත්වාකර්ෂණය (Acceleration due to gravity in m/s²)
    """
    theta_rad = np.radians(theta)  # අංශක රේඩියන් වලට පරිවර්තනය / Convert degrees to radians
    
    # කාලය ගණනය (Calculus: Time of flight) / Calculate time of flight
    t_flight = (2 * v0 * np.sin(theta_rad)) / g
    t = np.linspace(0, t_flight, 100)  # කාල ලකුණු 100ක් / 100 time steps
    
    # ස්ථාන සමීකරණ / Position equations (vector components)
    x = v0 * np.cos(theta_rad) * t  # තිරස් දුර / Horizontal distance
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2  # සිරස් උස / Vertical height
    
    # ප්‍රවේග සමීකරණ / Velocity equations
    vx = v0 * np.cos(theta_rad) * np.ones_like(t)  # තිරස් ප්‍රවේගය / Horizontal velocity
    vy = v0 * np.sin(theta_rad) - g * t  # සිරස් ප්‍රවේගය / Vertical velocity
    
    return t, x, y, vx, vy

# 2. Data Analysis with Pandas
def analyze_trajectory(t, x, y, vx, vy):
    """දත්ත විශ්ලේෂණය සහ DataFrame නිර්මාණය / Analyze data and create a DataFrame"""
    df = pd.DataFrame({
        'Time': t,
        'X_position': x,
        'Y_position': y,
        'X_velocity': vx,
        'Y_velocity': vy
    })
    
    # අමතර ගණනය කිරීම් / Additional calculations
    df['Velocity'] = np.sqrt(df['X_velocity']**2 + df['Y_velocity']**2)  # සම්පූර්ණ ප්‍රවේගය / Total velocity
    df['Acceleration'] = np.gradient(df['Velocity'], df['Time'])  # ත්වරණය / Acceleration
    
    analysis = {
        'Max Height': df['Y_position'].max(),       # උපරිම උස / Maximum height
        'Range': df['X_position'].iloc[-1],         # දුර / Horizontal range
        'Flight Time': df['Time'].iloc[-1],         # ගමන් කාලය / Total flight time
        'Impact Velocity': df['Velocity'].iloc[-1]  # භූමියට ඇදීමේ වේගය / Final impact velocity
    }
    
    return df, pd.Series(analysis)

# 3. Visualization
def plot_trajectory(df, title="Projectile Motion"):
    """ගමන් පථය ප්‍රස්තාර කිරීම / Plot the trajectory"""
    plt.figure(figsize=(10, 6))
    plt.plot(df['X_position'], df['Y_position'], 'b-', label='Trajectory')
    plt.title(title)
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Height (m)')
    plt.grid(True)
    plt.legend()
    plt.savefig("../data/projectile_trajectory.png")  # Save plot as an image
    plt.close()

def create_animation(x, y):
    """ගතිශීලී ඇනිමේෂන් / Create dynamic animation"""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    def update(frame):
        ax.clear()
        ax.plot(x[:frame], y[:frame], 'b-')
        ax.scatter(x[frame], y[frame], color='red', s=50)
        ax.set_xlim(0, max(x)*1.1)
        ax.set_ylim(0, max(y)*1.1)
        ax.grid(True)
        ax.set_title("Projectile Motion Animation")
        ax.set_xlabel("Horizontal Distance (m)")
        ax.set_ylabel("Vertical Height (m)")
        return ax
    
    anim = FuncAnimation(fig, update, frames=len(x), interval=50)
    anim.save("../data/projectile_motion_animation.gif", writer='pillow')  # Save animation as GIF
    plt.close()
    return HTML(anim.to_jshtml())  # Display in Jupyter


   
# 4. Main Execution
if __name__ == "__main__":
    try:
        # Get user input for initial velocity and angle
        v0 = float(input("Enter initial velocity (m/s): "))
        theta = float(input("Enter launch angle (degrees): "))
        
        # Perform calculations
        t, x, y, vx, vy = calculate_trajectory(v0, theta)
        
        # Analyze data
        df, analysis = analyze_trajectory(t, x, y, vx, vy)
        
        # Print results
        print("\nTrajectory Analysis:")
        print(analysis)
        
        # Save data to CSV
        df.to_csv('../data/projectile_data.csv', index=False)
        
        # Plot and save image
        plot_trajectory(df, f"Projectile (v0={v0} m/s, θ={theta}°)")
        
        # Create and display animation
        animation = create_animation(x, y)
        display(animation)

    except ValueError:
        print("⚠️ Please enter valid numeric values for velocity and angle.")
    
  
