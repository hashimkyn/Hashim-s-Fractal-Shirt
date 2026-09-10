Name: Hashim Abdullah
CMS ID: 551504
## Project Description
# Sakura & Rakaposhi — A Fractal Valley at Dusk
**Sakura & Rakaposhi** is an original fractal-based generative artwork that combines multiple fractal and recursive techniques into a single artistic composition.

The scene represents a dusk-lit valley inspired by the **Rakaposhi/Karakoram mountains of Hunza, Pakistan** and traditional **Japanese visual motifs**. Instead of using only one fractal pattern, the project combines four different fractal/self-similar construction techniques:

- Midpoint displacement for the mountain ridgelines
- Circular midpoint displacement for the imperfect Ensō moon
- Recursive branching with golden-angle phyllotaxis for the Sakura tree
- Recursive nested arcs and diamond subdivision for the Seigaiha river pattern and Hunza embroidery-inspired border

The final scene also includes animated falling petals and glowing lanterns to make the artwork more dynamic.

---

## Fractal Types Implemented

| Fractal / Technique | Implementation | Purpose |
|---|---|---|
| **1D Midpoint Displacement** | Recursive midpoint displacement with decreasing roughness | Karakoram mountain ridgelines |
| **Circular Midpoint Displacement** | Midpoint displacement applied around a circular path | Imperfect Ensō moon |
| **Recursive Branching** | L-system-style recursive branching | Sakura tree structure |
| **Golden-Angle Phyllotaxis** | 137.5° golden-angle placement | Sakura blossom clusters |
| **Recursive Nested Arcs** | Repeated self-similar semicircular arcs | Seigaiha river pattern |
| **Recursive Diamond Subdivision** | Smaller diamonds recursively generated from larger diamonds | Hunza embroidery-inspired border |

### 1. Mountain Ridgelines

The mountain layers are generated using **1D midpoint displacement**. A line segment is repeatedly divided at its midpoint, and a random vertical displacement is added.

The displacement decreases after every iteration, producing a natural-looking fractal terrain.

Three mountain layers are generated to create atmospheric depth and represent the Karakoram ridgeline, inspired by Rakaposhi, known as the **"Mother of Mist."**

### 2. Ensō Moon

The moon is created using **circular midpoint displacement**.

Instead of producing a mathematically perfect circle, points around the circle are repeatedly displaced perpendicular to the curve. This creates an intentionally imperfect outline inspired by the Japanese **Ensō** Zen circle.

### 3. Sakura Tree

The Sakura tree uses **recursive branching**.

Each branch recursively creates smaller branches until a specified depth is reached. Blossom clusters are then positioned using the **golden angle of approximately 137.5°**, which is associated with natural phyllotaxis patterns.

This combines recursive fractal branching with a mathematical arrangement inspired by patterns found in plants.

### 4. Seigaiha River

The river contains the Japanese **Seigaiha** wave pattern.

The pattern is constructed using repeated nested semicircular arcs. Multiple rows of these self-similar arcs create the appearance of continuous waves.

### 5. Hunza Embroidery Border

The top border uses a **recursive diamond subdivision** technique.

A large diamond is drawn and smaller diamonds are recursively positioned around it. Repeating this process creates a self-similar geometric lattice inspired by traditional Hunza embroidery geometry.

---

## Tools, Languages, and Libraries

| Tool / Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **NumPy** | Numerical calculations and coordinate generation |
| **Matplotlib** | 2D graphics, shapes, plotting, and animation |
| **Math** | Mathematical calculations such as angles and trigonometry |
| **Random** | Controlled random displacement and procedural generation |
| **VS Code / Python IDE** | Development environment |
## Image




