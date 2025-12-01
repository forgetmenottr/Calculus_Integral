from manim import *

class DefiniteIntegral(Scene):
    def construct(self):
        # --- 1. SETUP TEXT & FORMULAS ---
        title_RiemannSum = Text("Riemann Sum", font_size=36).to_edge(UP)
        title_DefiniteIntegral = Text("Definite Integral", font_size=36).to_edge(UP)
        
        riemann_formula = MathTex(
            r"\sum_{i=1}^{n} f(x_i) \cdot \Delta x", font_size=48
        )
        
        limit_formula = MathTex(
            r"\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x", font_size=48
        )
        
        full_integral_eq = MathTex(
            r"\int_{a}^{b} f(x) \, dx", 
            r"=", 
            r"\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x", 
            font_size=48
        )
        full_integral_eq[0].set_color(GREEN)
        full_integral_eq[2].set_color(BLUE)

        # --- 2. SETUP ĐỒ THỊ CHI TIẾT ---
        
        # 2.1 Hệ trục và Hàm số
        ax = Axes(
            x_range=[-0.5, 8.5], y_range=[-0.5, 6],
            x_length=10, y_length=5.5,
            axis_config={"include_tip": True, "color": GREY, "tip_width": 0.2, "tip_height": 0.2},
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")
        origin_label = MathTex("0", font_size=30).next_to(ax.c2p(0, 0), DL, buff=0.1)

        def func(x):
            return 0.05 * (x - 1) * (x - 4.5) * (x - 9) + 3.5

        a_val = 1.0
        dx = 0.8
        n_rects = 8
        b_val = a_val + n_rects * dx

        # Đồ thị chính
        graph = ax.plot(func, x_range=[a_val, b_val], color=BLUE_C, stroke_width=3)
        
        # Nhãn hàm số y=f(x) (sẽ hiện ra khi chuyển sang tích phân)
        label_func = MathTex("y=f(x)", font_size=30, color=WHITE).next_to(graph.point_from_proportion(0.5), UP, buff=0.5)

        # 2.2 Hình chữ nhật Riemann & Vùng Diện Tích (Area)
        # Hình chữ nhật (cho cảnh Riemann)
        rects = ax.get_riemann_rectangles(
            graph, x_range=[a_val, b_val], dx=dx, 
            input_sample_type="center",
            stroke_width=1.2, stroke_color=WHITE,
            fill_opacity=0.3, color=BLUE_B
        )
        
        # CẬP NHẬT: Vùng diện tích tô màu (cho cảnh Tích phân) - Màu xanh nhạt hài hòa
        area = ax.get_area(graph, x_range=[a_val, b_val], color=BLUE, opacity=0.4)

        # 2.3 Các nhãn trên trục x
        label_a = MathTex("a", font_size=32).next_to(ax.c2p(a_val, 0), DOWN, buff=0.15)
        tick_a = Line(ax.c2p(a_val, 0), ax.c2p(a_val, -0.1), color=WHITE)
        
        label_b = MathTex("b", font_size=32).next_to(ax.c2p(b_val, 0), DOWN, buff=0.15)
        tick_b = Line(ax.c2p(b_val, 0), ax.c2p(b_val, -0.1), color=WHITE)

        idx_i = 5 
        pos_xi = a_val + idx_i * dx
        pos_xim1 = a_val + (idx_i - 1) * dx
        
        lbl_xim1 = MathTex("x_{i-1}", font_size=28).next_to(ax.c2p(pos_xim1, 0), DOWN, buff=0.15)
        lbl_xi = MathTex("x_{i}", font_size=28).next_to(ax.c2p(pos_xi, 0), DOWN, buff=0.15)
        
        extra_labels = VGroup(
            lbl_xim1, lbl_xi,
            Line(ax.c2p(pos_xim1, 0), ax.c2p(pos_xim1, -0.1), color=WHITE),
            Line(ax.c2p(pos_xi, 0), ax.c2p(pos_xi, -0.1), color=WHITE),
        )

        # 2.4 Các nhãn điểm mẫu xi*
        star_labels = VGroup()
        xi_star_val = a_val + (idx_i - 0.5) * dx
        
        arrow_xi = Arrow(
            start=ax.c2p(xi_star_val, -0.8), end=ax.c2p(xi_star_val, -0.1), 
            buff=0, max_tip_length_to_length_ratio=0.15, color=GREY_B, stroke_width=2
        )
        lbl_xi_star = MathTex("x_i^*", font_size=28).next_to(arrow_xi, DOWN, buff=0.1)
        dash_xi = DashedLine(
            ax.c2p(xi_star_val, 0), ax.c2p(xi_star_val, func(xi_star_val)),
            dash_length=0.1, color=GREY_B, stroke_width=1.5
        )
        star_labels.add(arrow_xi, lbl_xi_star, dash_xi)

        # 2.5 Annotations
        rect_i = rects[idx_i - 1]
        brace_dx = Brace(rect_i, UP, buff=0.05, color=WHITE)
        label_dx = MathTex(r"\Delta x", font_size=28, color=YELLOW).next_to(brace_dx, UP, buff=0.1)

        brace_fx = Brace(
            Line(ax.c2p(xi_star_val, 0), ax.c2p(xi_star_val, func(xi_star_val))),
            RIGHT, buff=0.35, color=WHITE
        )
        label_fx = MathTex(r"f(x_i^*)", font_size=28, color=YELLOW).next_to(brace_fx, RIGHT, buff=0.1)

        annotations = VGroup(brace_dx, label_dx, brace_fx, label_fx)

        # 2.6 Gom nhóm đồ thị
        # Tách riêng các phần tử của Riemann để dễ fade out
        riemann_elements = VGroup(rects, extra_labels, star_labels, annotations)
        
        # Nhóm nền (luôn hiển thị)
        base_graph = VGroup(
            ax, labels, origin_label, graph,
            label_a, tick_a, label_b, tick_b
        )
        
        # Căn chỉnh vị trí: Đẩy đồ thị lên trên (UP) để nhãn xi* không bị trùng với công thức ở dưới
        graph_group = VGroup(base_graph, riemann_elements, area, label_func)
        graph_group.scale(0.85).move_to(ORIGIN).shift(UP * 0.5) 
        
        # Ban đầu area và label_func ẩn đi
        area.set_opacity(0)
        label_func.set_opacity(0)

        # --- 3. ANIMATION FLOW ---

        # Cảnh 1: Giới thiệu
        self.play(Write(title_RiemannSum), Write(riemann_formula))
        self.wait(1)

        # Cảnh 2: Đồ thị xuất hiện
        # Di chuyển công thức xuống dưới đáy
        self.play(
            riemann_formula.animate.scale(0.8).to_edge(DOWN, buff=0.5),
            FadeIn(base_graph),
            FadeIn(riemann_elements),
            run_time=2
        )
        self.wait(2)

        # Cảnh 3: Chuyển sang Tích phân (Transformation)
        
        # Chuẩn bị vị trí cho công thức giới hạn
        limit_formula.scale(0.8).move_to(riemann_formula)
        
        self.play(
            # 1. Đổi tiêu đề
            ReplacementTransform(title_RiemannSum, title_DefiniteIntegral),
            
            # 2. Đổi công thức
            ReplacementTransform(riemann_formula, limit_formula),
            
            # 3. Đổi đồ thị: Ẩn Riemann rời rạc -> Hiện vùng diện tích mịn
            FadeOut(riemann_elements), 
            area.animate.set_opacity(0.4), 
            FadeIn(label_func),
            
            run_time=2
        )
        self.wait(1)

        # Hiện đẳng thức cuối cùng
        full_integral_eq.scale(0.8).to_edge(DOWN, buff=0.5)
        self.play(
            ReplacementTransform(limit_formula, full_integral_eq[2]),
            FadeIn(full_integral_eq[0]),
            FadeIn(full_integral_eq[1])
        )
        
        self.wait(3)