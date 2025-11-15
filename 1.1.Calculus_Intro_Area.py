from manim import *

class CommonAreasEnglishScene(Scene):
    def construct(self):
        # --- 1. Rectangle ---
        
        # Title
        title_rect = Text("Rectangle Area", font_size=36).to_edge(UP)
        
        # Create shape and labels
        rect = Rectangle(width=5.0, height=3.0, color=BLUE, fill_opacity=0.5)
        w_label = MathTex("\\text{width} = 5").next_to(rect, DOWN)
        h_label = MathTex("\\text{height} = 3").next_to(rect, LEFT)
        
        # Formula
        formula_rect = MathTex(r"\text{Area} = \text{width} \times \text{height}", font_size=48).to_edge(DOWN)
        calc_rect = MathTex(r"\text{Area} = 5 \times 3 = 15", font_size=48).to_edge(DOWN)

        # Animations
        self.play(Write(title_rect))
        self.play(Create(rect))
        self.play(Write(w_label), Write(h_label))
        
        self.play(Write(formula_rect))
        self.wait(1.5)
        self.play(Transform(formula_rect, calc_rect))
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(rect),
            FadeOut(w_label),
            FadeOut(h_label),
            FadeOut(formula_rect),
            FadeOut(title_rect)
        )
        self.wait(0.5)

        # --- 2. Triangle ---
        
        # Title
        title_tri = Text("Triangle Area", font_size=36).to_edge(UP)
        
        # Create shape (right triangle for simplicity) and labels
        triangle = Polygon(
            [0, 0, 0], [4, 0, 0], [0, 3, 0], 
            color=GREEN, fill_opacity=0.5
        ).center()
        
        b_label = MathTex("\\text{base} = 4").next_to(triangle.get_bottom(), DOWN)
        h_label_tri = MathTex("\\text{height} = 3").next_to(triangle.get_left(), LEFT)
        
        # Formula
        formula_tri = MathTex(r"\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}", font_size=48).to_edge(DOWN)
        calc_tri = MathTex(r"\text{Area} = \frac{1}{2} \times 4 \times 3 = 6", font_size=48).to_edge(DOWN)

        # Animations
        self.play(Write(title_tri))
        self.play(Create(triangle))
        self.play(Write(b_label), Write(h_label_tri))
        
        self.play(Write(formula_tri))
        self.wait(1.5)
        self.play(Transform(formula_tri, calc_tri))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(triangle),
            FadeOut(b_label),
            FadeOut(h_label_tri),
            FadeOut(formula_tri),
            FadeOut(title_tri)
        )
        self.wait(0.5)

        # --- 3. Circle ---
        
        # Title
        title_circle = Text("Circle Area", font_size=36).to_edge(UP)
        
        # Create shape
        circle = Circle(radius=2.0, color=YELLOW, fill_opacity=0.5)
        
        # Radius line and label
        radius_line = Line(circle.get_center(), circle.get_right(), color=WHITE, stroke_width=3)
        r_label = MathTex("r = 2").next_to(radius_line, RIGHT, buff=0.2)
        
        # Formula
        formula_circle = MathTex(r"\text{Area} = \pi \times r^2", font_size=48).to_edge(DOWN)
        calc_circle = MathTex(r"\text{Area} = \pi \times 2^2 \approx 12.57", font_size=48).to_edge(DOWN)

        # Animations
        self.play(Write(title_circle))
        self.play(Create(circle))
        self.play(Create(radius_line), Write(r_label))
        
        self.play(Write(formula_circle))
        self.wait(1.5)
        self.play(Transform(formula_circle, calc_circle))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(circle),
            FadeOut(radius_line),
            FadeOut(r_label),
            FadeOut(formula_circle),
            FadeOut(title_circle)
        )
        
        # --- Concluding transition to Area Under a Curve ---
        final_text_part1 = Text(
            "But what about areas of irregular shapes?",
            font_size=38,
            t2c={"irregular shapes": YELLOW} 
        ).move_to(ORIGIN + UP * 1) # Move slightly up
        
        final_text_part2 = Text(
            "Like the area under a curve?",
            font_size=38,
           t2c={"area under a curve": GREEN} 
        ).move_to(ORIGIN + DOWN * 1) # Move slightly down

        self.play(Write(final_text_part1))
        self.wait(2)
        self.play(Write(final_text_part2))
        self.wait(3)
        self.play(FadeOut(final_text_part1), FadeOut(final_text_part2))