# 🎯 Projectile Motion Simulator

This project simulates and visualizes 2D projectile motion using Python. It includes physics calculations, data analysis, and dynamic animations.

## 📌 Features

- Calculates trajectory using calculus-based formulas
- Analyzes data using Pandas
- Generates plots with Matplotlib
- Creates animated motion (GIF + HTML)
- Saves data and visual outputs to files
- Interactive user input for velocity and launch angle

## 🚀 How to Run

### Requirements

Install the following Python libraries:

```bash
pip install numpy pandas matplotlib
```

Run the Script

```bash
cd scripts
python main.py
```

## 📊 Example Output

Trajectory Analysis:

```
Max Height : 127.55 m
Range : 1019.37 m
Flight Time : 14.43 s
Impact Velocity : 100.00 m/s
```

## 📷 Outputs

`projectile_data.csv`: Tabular motion data over time

`projectile_trajectory.png`: Static plot of the motion

`projectile_motion_animation.gif`: Animated trajectory

## 📚 Physics Behind

The simulation uses the standard kinematic equations:

`Horizontal motion: x = v0 _ cos(θ) _ t`

`Vertical motion: y = v0 _ sin(θ) _ t - 0.5 _ g _ t²`

Velocity components and resultant velocity are calculated for each time step.

## 🛠️ Author

Developed by Dhanushka Rathnayaka

- GitHub: https://github.com/Dhanuwa856

- portfolio: https://dhanushkarathnayakaportfolio.vercel.app/
