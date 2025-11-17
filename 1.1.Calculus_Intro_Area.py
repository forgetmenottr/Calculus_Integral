from manim import *

class IntroScene(Scene):
    def construct(self):
        # --- 1. AXES SETUP ---
        # Adjusted position: Reduced length and shifted DOWN to avoid overlapping with the title
        axes = Axes(
            x_range=[0, 1.3, 0.25],
            y_range=[0, 1.3, 0.25],
            x_length=5.5,  # Reduced from 6 to 5.5
            y_length=5.5,  # Reduced from 6 to 5.5
            axis_config={"include_numbers": True, "font_size": 24},
            tips=False,
        ).to_edge(LEFT, buff=1).shift(DOWN * 0.8) # Shifted down by 0.8 units
        
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Define the function y = x^2
        def func(x):
            return x**2

        graph = axes.plot(func, x_range=[0, 1.2], color=BLUE, stroke_width=4)
        
        # Moved label slightly to the right to ensure visibility
        graph_label = axes.get_graph_label(graph, label="y = x^2", x_val=1.2, direction=UP+LEFT)

        # --- 2. THE AREA PROBLEM ---
        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        
        # Highlight the area we want to find
        area = axes.get_area(graph, x_range=[0, 1], color=BLUE, opacity=0.3)
        # Position the question mark relative to the axes, not absolute coordinates
        question = Text("Area S = ?", font_size=36).move_to(axes.c2p(0.6, 0.3))
        
        self.play(FadeIn(area), Write(question))
        self.wait(2)
        self.play(FadeOut(area), FadeOut(question), FadeOut(graph_label))

        # --- 3. RIGHT ENDPOINT APPROXIMATION (n=4) ---
        # Title is at the top edge
        title_approx = Text("Approximating with Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title_approx))

        # FIX: Use string "right" for input_sample_type
        rects_right = axes.get_riemann_rectangles(
            graph, x_range=[0, 1], dx=0.25, stroke_width=2, stroke_color=WHITE, 
            input_sample_type="right", color=ORANGE, fill_opacity=0.6
        )
        
        self.play(Create(rects_right), run_time=2)
        
        # Position text relative to the right edge, but aligned better with the lower graph
        desc_right = Text("Right endpoints", font_size=24, color=ORANGE).to_edge(RIGHT, buff=1).shift(UP*1.5)
        
        # Show the calculation for R_4
        calc_text = MathTex(
            "Sum = 0.25(0.25^2 + 0.5^2 + 0.75^2 + 1^2)",
            font_size=28 # Slightly smaller font to fit
        ).next_to(desc_right, DOWN)
        
        result_text = MathTex(
            "\\approx 0.46875",
            color=ORANGE,
            font_size=36
        ).next_to(calc_text, DOWN)
        
        # Point out the error (overestimate)
        arrow = Arrow(start=RIGHT, end=LEFT, color=RED).next_to(rects_right, RIGHT, buff=0.1).shift(UP*0.5)
        over_text = Text("Overestimate!", font_size=24, color=RED).next_to(arrow, RIGHT)

        self.play(FadeIn(desc_right))
        self.play(Write(calc_text), Write(result_text))
        self.play(Create(arrow), Write(over_text))
        self.wait(2)

        # Clean up for the next part
        self.play(
            FadeOut(rects_right), FadeOut(calc_text), FadeOut(result_text), 
            FadeOut(arrow), FadeOut(over_text), FadeOut(desc_right)
        )

        # --- 4. LEFT ENDPOINT APPROXIMATION (n=4) ---
        
        rects_left = axes.get_riemann_rectangles(
            graph, x_range=[0, 1], dx=0.25, stroke_width=2, stroke_color=WHITE, 
            input_sample_type="left", color=GREEN, fill_opacity=0.6
        )
        
        desc_left = Text("Left endpoints", font_size=24, color=GREEN).to_edge(RIGHT, buff=1).shift(UP*1.5)
        
        self.play(Create(rects_left), run_time=2)
        self.play(FadeIn(desc_left))

        # Show the calculation for L_4
        result_text_l = MathTex(
            "Sum \\approx 0.21875",
            color=GREEN,
            font_size=36
        ).next_to(desc_left, DOWN)

        over_text_l = Text("Underestimate!", font_size=24, color=YELLOW).next_to(result_text_l, DOWN)

        self.play(Write(result_text_l))
        self.play(Write(over_text_l))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(rects_left), FadeOut(result_text_l), 
            FadeOut(over_text_l), FadeOut(desc_left)
        )

        # --- 5. INCREASING THE NUMBER OF RECTANGLES ---
        
        new_title = Text("How to get a better approximation?", font_size=36).to_edge(UP)
        self.play(Transform(title_approx, new_title))

        n_tracker = ValueTracker(4)
        
        def get_rects():
            n = int(n_tracker.get_value())
            dx = 1 / n
            return axes.get_riemann_rectangles(
                graph, x_range=[0, 1], dx=dx, stroke_width=0.5, 
                input_sample_type="right", color=BLUE_C, fill_opacity=0.5
            )

        rects_anim = always_redraw(get_rects)
        self.add(rects_anim)

        # Display 'n' on the right side
        n_display = Integer(4).to_edge(RIGHT, buff=2).shift(UP)
        n_label = Text("n = ", font_size=30).next_to(n_display, LEFT)
        
        n_display.add_updater(lambda m: m.set_value(n_tracker.get_value()))

        self.play(Write(n_label), Write(n_display))
        self.wait()

        # Animate 'n' increasing
        self.play(n_tracker.animate.set_value(50), run_time=4, rate_func=linear)
        
        final_area_text = Text("Area approaches 1/3", color=YELLOW, font_size=36).next_to(n_display, DOWN, buff=0.5)
        self.play(Write(final_area_text))
        self.wait(2)

        # --- 6. INTRODUCING THE RIEMANN SUM ---
        
        # Clean up old text
        self.play(
            FadeOut(final_area_text), 
            FadeOut(n_label), 
            FadeOut(n_display),
            FadeOut(title_approx)
        )

        # Formal Title
        formal_title = Title("The Riemann Sum", font_size=40).to_edge(UP)
        self.play(Write(formal_title))

        # Sigma Formula
        sigma_formula = MathTex(
            r"\text{Area} \approx \sum_{i=1}^{n} f(x_i) \Delta x",
            font_size=40
        ).to_edge(RIGHT, buff=1).shift(UP)

        explanation = Text("Sum of n rectangles", font_size=24, color=BLUE_C).next_to(sigma_formula, DOWN)

        self.play(Write(sigma_formula))
        self.play(FadeIn(explanation))
        self.wait(2)

        # Limit Definition
        limit_formula = MathTex(
            r"\text{Area} = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x",
            font_size=40
        ).move_to(sigma_formula)

        limit_explanation = Text("The Definite Integral", font_size=24, color=YELLOW).next_to(limit_formula, DOWN)

        self.play(
            Transform(sigma_formula, limit_formula),
            Transform(explanation, limit_explanation)
        )
        self.wait(1)

        # Integral Notation
        integral_symbol = MathTex(
            r"\int_{0}^{1} x^2 \,dx = \frac{1}{3}",
            font_size=50, color=YELLOW
        ).next_to(limit_explanation, DOWN, buff=0.5)

        box = SurroundingRectangle(integral_symbol, color=YELLOW)

        self.play(Write(integral_symbol), Create(box))
        
        # Show smooth area
        self.remove(rects_anim)
        smooth_area = axes.get_area(graph, x_range=[0, 1], color=BLUE, opacity=0.5)
        self.play(FadeIn(smooth_area))
        
        self.wait(3)