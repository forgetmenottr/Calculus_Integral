from manim import *

class CommonAreasFastScene(Scene):
    def construct(self):
        # --- Setup Shapes & Formulas ---
        
        # 1. Rectangle
        rect = Rectangle(width=3.0, height=2.0, color=BLUE, fill_opacity=0.5)
        rect_label = MathTex(r"A = w \times h", font_size=36).next_to(rect, DOWN)
        rect_group = VGroup(rect, rect_label)

        # 2. Triangle
        triangle = Triangle(color=GREEN, fill_opacity=0.5).scale(1.5)
        tri_label = MathTex(r"A = \frac{1}{2}bh", font_size=36).next_to(triangle, DOWN)
        tri_group = VGroup(triangle, tri_label)

        # 3. Circle
        circle = Circle(radius=1.2, color=YELLOW, fill_opacity=0.5)
        circ_label = MathTex(r"A = \pi r^2", font_size=36).next_to(circle, DOWN)
        circ_group = VGroup(circle, circ_label)

        # Arrange them in a row
        shapes = VGroup(rect_group, tri_group, circ_group).arrange(RIGHT, buff=1.5)
        
        # Title
        title = Text("Standard Areas", font_size=48).to_edge(UP)

        # --- Animation Sequence (Total ~8-10 seconds) ---

        # 1. Intro Title (1s)
        self.play(Write(title), run_time=0.8)

        # 2. Show all shapes and formulas rapidly (2s)
        # LaggedStart makes them appear one after another very quickly
        self.play(
            LaggedStart(
                FadeIn(rect_group, shift=UP),
                FadeIn(tri_group, shift=UP),
                FadeIn(circ_group, shift=UP),
                lag_ratio=0.3
            ),
            run_time=2
        )
        
        # 3. Pause for viewer to digest (2s)
        self.wait(2)
        
        self.play(
            FadeOut(shapes, target_position=DOWN),
            FadeOut(title),
            run_time=1.5
        )
        
        self.wait(1)
        
        # --- Concluding transition to Area Under a Curve ---
        final_text_part1 = Text(
            "But what about areas of irregular shapes?",
            font_size=38,
            t2c={"irregular shapes": YELLOW} 
        ).move_to(ORIGIN + UP * 1) # Move slightly up
        

        self.play(Write(final_text_part1))
        self.wait(1)
        self.play(FadeOut(final_text_part1))
        
        final_text_part2 = Text(
            "Like the area under a curve?",
            font_size=38,
            t2c={"area under a curve": GREEN}
            ).move_to(ORIGIN)
        self.play(FadeIn(final_text_part2, shift=UP))
        
        # --- 4. Show three different curves with shaded area ---
        def make_axes():
            return Axes(
                x_range=[0, 6, 1],
                y_range=[0, 8, 1],
                axis_config={"include_tip": True},
                x_length=4,
                y_length=3
            )

        # 3 axes
        axes1 = make_axes()
        axes2 = make_axes()
        axes3 = make_axes()

        # functions
        graph1 = axes1.plot(lambda x: -0.4*(x-3)**2 + 6, color=BLUE)
        graph2 = axes2.plot(lambda x: -0.1*(x-3)**3 + 0.6*(x-3) + 5, color=GREEN)
        graph3 = axes3.plot(lambda x: -0.02*(x-3)**4 + 0.25*(x-3)**2 + 6, color=YELLOW)

        # areas
        area1 = axes1.get_area(graph1, x_range=[1.5, 4.5], color=BLUE, opacity=0.6)
        area2 = axes2.get_area(graph2, x_range=[1, 5], color=GREEN, opacity=0.6)
        area3 = axes3.get_area(graph3, x_range=[1, 5], color=YELLOW, opacity=0.6)

        # chịu
        top_row = Group(
            VGroup(axes1, graph1, area1),
            VGroup(axes2, graph2, area2)
        ).arrange(RIGHT, buff=1.2)

        bottom_row = VGroup(axes3, graph3, area3)

        layout = Group(top_row, bottom_row).arrange(DOWN, buff=1.2)

        # animations
        self.play(Create(axes1), Create(axes2), Create(axes3))
        self.wait(0.1)

        self.play(Create(graph1), Create(graph2), Create(graph3))
        self.wait(0.1)

        self.play(FadeIn(area1), FadeIn(area2), FadeIn(area3))
        self.wait(0.5)
        
        #end scene
        everything = VGroup(
            axes1, axes2, axes3,
            graph1, graph2, graph3,
            area1, area2, area3,
            final_text_part2
            )
        self.play(FadeOut(everything))
        self.wait(1)
        