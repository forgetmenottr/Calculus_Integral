from manim import *

class IntegralDefinitionIntro(Scene):
    def construct(self):
        # --- Choose interval ---
        a = 1
        b = 3

        # === Coordinate Axes ===
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 30, 5],
            x_length=6,
            y_length=4,
            axis_config={"include_ticks": False, "include_numbers": False, "color": GREY},
            tips=True,
        ).move_to(ORIGIN)

        # === Labels ===
        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        y_label = MathTex("y").next_to(axes.y_axis, UP)

        # === Title ===
        title = Text("Example of Definite Integral", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # === Draw axes ===
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # === Define function f(x) ===
        def f(x):
            return x**3 - x + 2

        graph = axes.plot(f, x_range=[a, b], color=BLUE)

        # === Label f(x) ===
        graph_label = axes.get_graph_label(graph, label="f(x)", x_val=b)

        # === Mark points a and b on x-axis ===
        a_dot = Dot(axes.c2p(a, 0), color=RED)
        b_dot = Dot(axes.c2p(b, 0), color=RED)
        a_label = MathTex("a").next_to(a_dot, DOWN)
        b_label = MathTex("b").next_to(b_dot, DOWN)

        # === Draw graph ===
        self.play(Create(graph), Write(graph_label))
        self.wait(0.5)

        self.play(FadeIn(a_dot), Write(a_label), FadeIn(b_dot), Write(b_label))
        self.wait(2)
