from manim import *

class RiemannSumIntroScene(Scene):
    def construct(self):
        # --- 1. AXES SETUP ---
        # Adjusted position: Reduced length and shifted DOWN to avoid overlapping with the title
        title_problem = Text("The Area Problem", font_size=36).to_edge(UP)
        axes = Axes(
            x_range=[0, 1.3, 0.25],
            y_range=[0, 1.3, 0.25],
            x_length=5.5,  # Reduced from 6 to 5.5
            y_length=5.5,  # Reduced from 6 to 5.5
            axis_config={"include_numbers": True, "font_size": 24},
            tips=True,
        ) # Shifted down by 0.8 units
        
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Define the function y = x^2
        def func(x):
            return x**2

        graph = axes.plot(func, x_range=[0, 1.2], color=BLUE, stroke_width=4)
        
        # Moved label slightly to the right to ensure visibility
        graph_label = axes.get_graph_label(graph, label="y = x^2", x_val=1.2, direction=UP+LEFT)
        
        graph_group = VGroup(axes, labels, graph, graph_label)
        graph_group.center().shift(DOWN * 0.5)

        # --- 2. THE AREA PROBLEM ---
        self.play(Write(title_problem))
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
        self.play(
            ReplacementTransform(title_problem, title_approx),
            graph_group.animate.to_edge(LEFT, buff=1).shift(DOWN * 0.02)
        )
        self.wait(1)

        # FIX: Use string "right" for input_sample_type
        rects_right = axes.get_riemann_rectangles(
            graph, x_range=[0, 1], dx=0.25, stroke_width=2, stroke_color=WHITE, 
            input_sample_type="right", color=ORANGE, fill_opacity=0.6
        )
        
        self.play(Create(rects_right), run_time=2)
        
        # Position text relative to the right edge, but aligned better with the lower graph
 # Fixed positioning: Anchored to graph_group, not to_edge(RIGHT)
        # We align the top of this text block to the top of the graph_group
        desc_right = Text("Right endpoints", font_size=24, color=ORANGE)
        desc_right.next_to(graph_group, RIGHT, buff=0.5).align_to(graph_group, UP)
 
        # Show the calculation for R_4
        calc_text = MathTex(
            "Sum = 0.25(0.25^2 + 0.5^2 + 0.75^2 + 1^2)",
            font_size=28 # Slightly smaller font to fit
        ).next_to(desc_right, DOWN, buff=0.25, aligned_edge=LEFT)
        
        result_text = MathTex(
            "\\approx 0.46875",
            color=ORANGE,
            font_size=36
        ).next_to(calc_text, DOWN, buff=0.25, aligned_edge=LEFT)
        
        # Point out the error (overestimate)
        # Positioned relative to the rectangles themselves
        arrow = Arrow(start=RIGHT, end=LEFT, color=RED).next_to(rects_right, RIGHT, buff=0.1).shift(UP*0.5)
        over_text = Text("Overestimate!", font_size=24, color=RED).next_to(arrow, RIGHT)

        self.play(FadeIn(desc_right))
        self.play(Write(calc_text))
        self.play(Write(result_text))
        self.play(Create(arrow), Write(over_text))
        self.wait(3) # Wait at the end
        
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
        
        desc_left = Text("Left endpoints", font_size=24, color=GREEN)
        desc_left.next_to(graph_group, RIGHT, buff=0.5).align_to(graph_group, UP)
        
        self.play(Create(rects_left), run_time=2)
        self.play(FadeIn(desc_left))

        # Show the calculation for L_4
        calc_text_l = MathTex(
            "Sum = 0.25(0^2 + 0.25^2 + 0.5^2 + 0.75^2)",
            font_size=28 # Slightly smaller font to fit
        ).next_to(desc_left, DOWN, buff=0.25, aligned_edge=LEFT)
        
        result_text_l = MathTex(
            "Sum \\approx 0.21875",
            color=GREEN,
            font_size=36
        ).next_to(calc_text_l, DOWN, buff=0.25, aligned_edge=LEFT)
        
        #arrow left
        arrow_l = Arrow(start=RIGHT, end=LEFT, color=RED).next_to(rects_left, RIGHT, buff=0.1).shift(UP*0.5)
        
        over_text_l = Text("Underestimate!", font_size=24, color=RED).next_to(arrow_l, RIGHT)
        
        self.play(Write(calc_text_l))
        self.play(Write(result_text_l))
        self.play(Create(arrow_l))
        self.play(Write(over_text_l))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(rects_left), FadeOut(result_text_l), FadeOut(calc_text_l),
            FadeOut(over_text_l), FadeOut(desc_left), FadeOut(arrow_l)
        )
        
        # --- 6. SCENE 5: HOW TO GET A BETTER APPROXIMATE ---

        # New title
        title_better_approx = Text("How to get a better approximate?", font_size=36).to_edge(UP)

        # Re-show the graph group and the new title
        # The graph_group is still at its last position (to_edge(LEFT, ...))
        self.play(
            ReplacementTransform(title_approx, title_better_approx),
        )
        self.wait(1)
        
        # Data (raw strings)
        table_data_strings = [
            ("10", "0.3850000"),
            ("20", "0.3587500"),
            ("30", "0.3501852"),
            ("50", "0.3434000"),
            ("100", "0.3383500"),
            ("1000", "0.3338335"),
        ]
        
        # --- NEW HYBRID LOGIC ---

        # 1. Create the DATA table (using regular Table)
        data_table = Table(
            table_data_strings,
            include_outer_lines=True,
            h_buff=0.4,
            v_buff=0.2,
            line_config={"stroke_width": 1},
            # This config applies to the strings in table_data_strings
            element_to_mobject_config={"font": "Consolas", "font_size": 24}
        )
        
        # Position the data table (make space for header)
        data_table.next_to(graph_group, RIGHT, buff=0.5).shift(DOWN * 1.0)
        
        # 2. Create MathTex headers SEPARATELY
        header_n = MathTex("n", font_size=28, stroke_width=1, color=WHITE)
        header_Rn = MathTex("R_n", font_size=28, stroke_width=1, color=WHITE)
        
        # 3. Manually position headers above the columns
        # Get the top center of the first and second columns
        col_1_top = data_table.get_columns()[0].get_top()
        col_2_top = data_table.get_columns()[1].get_top()
        
        # Place headers right above their columns
        header_n.next_to(col_1_top, UP, buff=0.25)
        header_Rn.next_to(col_2_top, UP, buff=0.25)

        # --- Animation Sequence ---
        
        # 3.1. Create grid lines first (This works now!)
        # 3.1. Create grid lines first (FIXED)
        table_lines = VGroup(
            *data_table.get_horizontal_lines(),
            *data_table.get_vertical_lines()
        )
        self.play(Create(table_lines))

        # 3.2. Write headers
        self.play(Write(header_n), Write(header_Rn))
        self.wait(0.5)

        # 3.3. Get data entries (These are now inside data_table)
        data_row_mobjects = data_table.get_rows()

        # --- Loop Animation ---
        
        # 3.4. Show first row (n=10) and initial rects
        n_initial = int(table_data_strings[0][0])
        current_rects = axes.get_riemann_rectangles(
                graph, x_range=[0, 1], dx=1.0/n_initial, input_sample_type="right",
                color=ORANGE, fill_opacity=0.6, stroke_width=2.0
        )
        # Animate the rects and the first data row
        self.play(Create(current_rects), Write(data_row_mobjects[0]))
        self.wait(1)

        # 3.5. Loop through the rest of the data
        for i in range(1, len(table_data_strings)):
            n_val = int(table_data_strings[i][0])
            new_rects = axes.get_riemann_rectangles(
                graph, x_range=[0, 1], dx=1.0/n_val, input_sample_type="right",
                color=ORANGE, fill_opacity=0.6 + (i*0.05),
                stroke_width=max(1.5 * (0.7**i), 0.05) 
            )
            
            # Play transform of rects and write new row simultaneously
            self.play(
                ReplacementTransform(current_rects, new_rects),
                Write(data_row_mobjects[i]), # Write the next data row
                run_time=0.8 
            )
            self.wait(0.5)
            current_rects = new_rects
            
        self.wait(1)
        
            # clean
        self.play(
            FadeOut(data_row_mobjects),FadeOut(table_lines), FadeOut(header_n), FadeOut(header_Rn),
            FadeOut(current_rects), FadeOut(new_rects)
        )
        self.wait(1)