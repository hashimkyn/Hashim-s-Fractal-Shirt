# Sakura & Rakaposhi — A Fractal Valley at Dusk

## Project Description

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

### Required Libraries

```bash
pip install numpy matplotlib
```

---

## Project Structure

```text
Sakura-Rakaposhi/
│
├── fractal_valley.py
├── README.md
└── fractal_valley.png
```

- `fractal_valley.py` — Main Python program containing all fractal algorithms and scene generation.
- `README.md` — Project documentation.
- `fractal_valley.png` — Screenshot/static output of the generated fractal artwork.

---

## Setup and Run Instructions

### Step 1 — Install Python

Make sure Python 3.x is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2 — Clone or Download the Project

Clone the project repository:

```bash
git clone <your-github-repository-url>
```

Navigate into the project folder:

```bash
cd Sakura-Rakaposhi
```

### Step 3 — Install Required Libraries

Run:

```bash
pip install numpy matplotlib
```

### Step 4 — Run the Program

Run the Python file:

```bash
python fractal_valley.py
```

A Matplotlib window will open and display the generated fractal valley.

The scene includes animation for:

- Falling Sakura petals
- Glowing lanterns

---

## Screenshot / Output

The generated artwork should look similar to the following composition:

```text
┌───────────────────────────────────────────────────────────┐
│                    Sakura & Rakaposhi                     │
│                                                           │
│                    ◯  Ensō Moon                           │
│             /\        /\       /\                        │
│        /\  /  \  /\  /  \ /\ /  \                       │
│       /  \/    \/  \/    V  V    \                       │
│                                                           │
│                    🌸 Sakura Tree                         │
│                       │                                   │
│                      /│\                                  │
│                     / │ \                                 │
│                    /  │  \                                │
│                                                           │
│             🏔️ Karakoram Mountain Layers                 │
│                                                           │
│ ~~~~~~~~ Seigaiha / Turquoise Glacial River ~~~~~~~~~~~~ │
│                                                           │
│   ◇◇◇◇◇◇◇◇◇ Hunza Embroidery Lattice ◇◇◇◇◇◇◇◇◇       │
└───────────────────────────────────────────────────────────┘
```

### Actual Project Screenshot

Place your generated screenshot in the project folder and name it:

```text
fractal_valley.png
```

Then add it to this README using:

```markdown
![Sakura & Rakaposhi Fractal Artwork](fractal_valley.png)
```

For GitHub, the screenshot will appear here:

![Sakura & Rakaposhi Fractal Artwork](fractal_valley.png)

---

## Key Features

- Multiple fractal techniques combined into one composition
- Procedural mountain generation
- Recursive tree generation
- Golden-angle blossom placement
- Imperfect circular Ensō generation
- Recursive Japanese Seigaiha wave pattern
- Recursive diamond lattice pattern
- Dusk gradient background
- Animated falling petals
- Animated glowing lanterns
- Uses deterministic random seeds for reproducible fractal structures
- Original combination of mathematical patterns and cultural visual motifs

---

## Mathematical Concepts

The project demonstrates several concepts from computer graphics and fractal geometry:

### Midpoint Displacement

A line segment is repeatedly divided at its midpoint and the midpoint is randomly displaced.

```text
        /\          /\ 
       /  \   →    /  \__
______/    \______/
```

As the number of iterations increases and the displacement decreases, increasingly detailed terrain is produced.

### Recursive Branching

The Sakura tree follows the recursive idea:

```text
Branch
 ├── Branch
 │    ├── Branch
 │    └── Branch
 └── Branch
      ├── Branch
      └── Branch
```

Each generation produces smaller branches until the maximum recursion depth is reached.

### Golden Angle

The blossoms use an angle of approximately:

```text
137.5°
```

This creates a natural-looking distribution of blossom points around branch ends.

### Self-Similarity

The Seigaiha waves and diamond lattice demonstrate **self-similarity**, where smaller structures resemble the larger structure from which they are generated.

---

## Animation

The project goes beyond a static fractal rendering.

During execution:

- Sakura petals continuously fall through the scene.
- Petals move slightly from side to side to simulate natural movement.
- Lanterns change their brightness over time.
- Petals that reach the bottom are repositioned at the top.

The animation is implemented using Matplotlib's `FuncAnimation`.

---

## Cultural Inspiration

The project combines visual inspiration from two regions.

### Japan

- **Ensō** — represented by the imperfect circular moon.
- **Seigaiha** — represented through the recursive wave pattern.
- **Ukiyo-e-inspired aesthetics** — reflected through the indigo and gold palette.

### Hunza Valley, Pakistan

- **Rakaposhi / Karakoram mountains** — represented through fractal mountain ridgelines.
- **Apricot blossom season** — represented through the Sakura-inspired flowering tree and falling petals.
- **Turquoise glacial river** — represented through the river section.
- **Traditional embroidery geometry** — represented through the recursive diamond lattice.

---

## Student Information

| Information | Details |
|---|---|
| **Student Name** | YOUR NAME |
| **Registration Number** | YOUR REGISTRATION NUMBER |
| **Course** | Computer Graphics / Fractal Design |
| **Project Title** | Sakura & Rakaposhi — A Fractal Valley at Dusk |

---

## Conclusion

**Sakura & Rakaposhi** demonstrates how fractal mathematics can be used not only to generate traditional mathematical patterns but also to create an original artistic composition.

By combining midpoint displacement, circular displacement, recursive branching, golden-angle phyllotaxis, nested arcs, and recursive diamond subdivision, the project creates a single interactive fractal landscape inspired by Japanese and Hunza visual traditions.

The project therefore demonstrates both the **mathematical concepts of fractals and recursion** and their application in **computer-generated visual art**.