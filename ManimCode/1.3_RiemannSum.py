from manim import *
# ựa lười ghi lại code quá nên lúc edit nhớ cắt phần đầu ra giùm nhé ^^

class RiemannSumIntroScene(Scene):
    def construct(self):
        # --- 1. AXES SETUP ---
        # Adjusted position: Reduced length and shifted DOWN to avoid overlapping with the title
        title_better_approx = Text("How to get a better approximate?", font_size=36).to_edge(UP)
        self.play(Write(title_better_approx))
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
        self.play(
            graph_group.animate.to_edge(LEFT, buff=1).shift(DOWN * 0.02)
        )
        
        self.wait(1)
        
        # Xuất hiện 4 hình chữ nhật màu đỏ right-endpoint nằm trong đồ thị
        rects_R4_initial = axes.get_riemann_rectangles(
            graph, x_range=[0, 1], dx=0.25, 
            input_sample_type="right", color=RED, fill_opacity=0.6 
        )
        self.play(Create(rects_R4_initial))
        self.wait(1)
        
        
        
# --- NEW SCENE ---

        # 1. Prepare object
        # Grouping and locating
        equation_group = VGroup()
        
        # List of rectangles
        # and text (dùng cho FadeIn/Write)
        moved_rects = VGroup()
        labels_and_signs = VGroup()

        # Grouping (Hình + f(x) + dx)
        for rect in rects_R4_initial:
            # Copying
            new_rect = rect.copy().set_color(RED).set_fill(color=RED, opacity=1.0)
            
            # f(x) between rectangles
            f_x_label = MathTex("f(x)", font_size=24, color=WHITE).move_to(new_rect.get_center())
            
            # dx below
            dx_label = MathTex("dx", font_size=24, color=WHITE).next_to(new_rect, DOWN, buff=0.1)
            
            # grouping
            term_group = VGroup(new_rect, f_x_label, dx_label)
            
            # Thêm vào danh sách quản lý
            equation_group.add(term_group)
            moved_rects.add(new_rect)
            labels_and_signs.add(f_x_label, dx_label)

        # adding +
        plus_signs = VGroup()
        
        # kbic
        full_sum_mobject = VGroup()
        
        for i in range(len(equation_group)):
            full_sum_mobject.add(equation_group[i])
            if i < len(equation_group) - 1:
                plus = MathTex("+", font_size=40)
                plus_signs.add(plus)
                labels_and_signs.add(plus)
                full_sum_mobject.add(plus)

        # Rearrange
        full_sum_mobject.arrange(RIGHT, buff=0.2).center()
        
        # Make text
        area_text = MathTex("Area =", font_size=40).next_to(full_sum_mobject, LEFT, buff=0.5)

        # --- (ANIMATION) ---
        
        # Biến đổi hình chữ nhật từ đồ thị ra giữa màn hình
        self.play(
            FadeOut(graph_group),
            ReplacementTransform(rects_R4_initial, moved_rects), 
            Write(area_text),
            run_time=1.5
        )
        
        self.wait(0.5)

        # Hiện các nhãn f(x), dx và dấu cộng
        self.play(
            Write(labels_and_signs),
            run_time=1
        )
        
        self.wait(1)

        # 4 hình chữ nhật này biến thành công thức sigma
        formula_sigma_img2 = MathTex(
            r"Area = \sum_{i=1}^{4} f(x_i) \cdot dx",
            font_size=50
        )
        # Di chuyển công thức sigma sang bên phải
        formula_sigma_img2.next_to(graph_group, RIGHT, buff=1.0)

        # Tạo lại các hình chữ nhật để hiển thị cùng đồ thị
        final_rects = axes.get_riemann_rectangles(
            graph, x_range=[0, 1], dx=0.25, 
            input_sample_type="right", color=RED, fill_opacity=0.6
        )
        
        # ựa
        self.play(
            ReplacementTransform(VGroup(area_text, full_sum_mobject), formula_sigma_img2),
            FadeIn(graph_group),
            Create(final_rects)
        )
        self.wait(0.5)

# --- RIEMANN SUM ---
        COMMON_FONT_SIZE = 50

        # 1st formula n=4
        current_formula = MathTex(
            r"Area = \sum_{i=1}^{4} f(x_i) \cdot dx", 
            font_size=COMMON_FONT_SIZE
        )
        
        # Position 1st formula
        current_formula.next_to(graph_group, RIGHT, buff=0.5)
        
        # kbic
        if 'formula_sigma_img2' in locals():
            self.remove(formula_sigma_img2)
            current_formula.move_to(formula_sigma_img2, aligned_edge=LEFT)
        
        self.add(current_formula)

        # --- BẮT ĐẦU VÒNG LẶP TĂNG N ---

        n_values = [8, 16, 32, 64]
        current_rects = final_rects
        
        for n in n_values:
            # cthuc tăng theo hcn
            new_rects = axes.get_riemann_rectangles(
                graph, x_range=[0, 1], dx=1.0/n, 
                input_sample_type="right", color=RED, fill_opacity=0.6
            )
            new_formula = MathTex(
                r"Area = \sum_{i=1}^{" + str(n) + r"} f(x_i) \cdot dx",
                font_size=COMMON_FONT_SIZE
            )
            
            new_formula.move_to(current_formula, aligned_edge=LEFT)

            # Animation
            self.play(
                ReplacementTransform(current_rects, new_rects),
                ReplacementTransform(current_formula, new_formula),
                run_time=1.0
            )

            # Update variable
            current_rects = new_rects
            current_formula = new_formula
            
            self.wait(0.5)

        # --- LAST DANCE ---

        # OVERALL
        final_generic_formula = MathTex(
            r"\sum_{i=1}^{n} f(x_i) \cdot dx",
            font_size=50
        ).center()
        
        title_RiemannSum= Text("Riemann Sum", font_size=36).to_edge(UP)
        
        # Animation
        self.play(
            ReplacementTransform(title_better_approx,title_RiemannSum),
            ReplacementTransform(current_formula, final_generic_formula),
            FadeOut(graph_group),
            FadeOut(axes),
            FadeOut(current_rects),
            run_time=2.0
        )

        self.wait(2)