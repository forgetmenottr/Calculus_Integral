from manim import *
import numpy as np

class FundamentalTheoremComplete(Scene):
    def construct(self):
        # ==================== FUNCTION AND NUMERICAL VALUES ====================
        def func(x):
            return 0.05 * (x - 1) * (x - 4.5) * (x - 9) + 3.5

        a_val = 1.0
        dx = 0.8
        n_rects = 8
        b_val = a_val + n_rects * dx  # b_val = 1.0 + 8 * 0.8 = 7.4

        # ==================== SETUP AXES AND GRAPH ====================
        
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 6, 1],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True, "include_numbers": False},
        ).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        origin_label = MathTex("0", font_size=30).next_to(axes.c2p(0, 0), DL, buff=0.1)

        # Plot the function
        graph = axes.plot(
            func, 
            x_range=[0, 10], 
            color=BLUE,
            stroke_width=3
        )

        # ==================== PLACE LABEL IN THE RED REGION ====================
        # Choose a fixed position inside the circled red area
        label_target_point = axes.c2p(5.0, 4.2)

        graph_label = (
            MathTex("y = f(x)", color=BLUE, font_size=42)
            .move_to(label_target_point)
        )

        
        # ==================== PART I: DEFINITE INTEGRAL ====================
        # Create bound lines and labels
        a_line = axes.get_vertical_line(axes.c2p(a_val, 0), color=YELLOW, stroke_width=4)
        b_line = axes.get_vertical_line(axes.c2p(b_val, 0), color=YELLOW, stroke_width=4)
        
        a_label = MathTex("a", color=YELLOW, font_size=40).next_to(
            axes.c2p(a_val, 0), DOWN, buff=0.2
        )
        b_label = MathTex("b", color=YELLOW, font_size=40).next_to(
            axes.c2p(b_val, 0), DOWN, buff=0.2
        )
        
        # Shaded area between a and b
        area_fixed = axes.get_area(
            graph,
            x_range=[a_val, b_val],
            color=[BLUE, GREEN],
            opacity=0.6
        )
        
        # Definite integral formula
        definite_integral = MathTex(
            r"\int_a^b f(x) \, dx",
            font_size=50
        ).to_edge(UP, buff=0.5)
        
        # Animate Part I
        self.play(
        Create(axes),
        Create(graph), Write(graph_label))
        self.wait(0.5)
        
        self.play(
            Create(a_line),
            Create(b_line),
            Write(a_label),
            Write(b_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(Write(definite_integral), run_time=0.5)        
        self.play(FadeIn(area_fixed), run_time=2)
        self.wait(2)