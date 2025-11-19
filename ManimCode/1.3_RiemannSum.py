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
            input_sample_type="right", color=RED, fill_opacity=0.6 # Màu đỏ như bạn mô tả
        )
        self.play(Create(rects_R4_initial))
        self.wait(1)
        
        
        # 4 hình chữ nhật di chuyển ra ngoài, có dấu cộng nằm giữa mỗi hình, 
        # f(x) bên trong mỗi hình và phía dưới ghi dx giống hình 1
        
        # Tạo bản sao của các hình chữ nhật để di chuyển ra ngoài
        moved_rects = VGroup(*[rect.copy().set_color(RED).set_fill(color=RED, opacity=1.0) for rect in rects_R4_initial])

        # Tạo các nhãn f(x) và dx cho mỗi hình chữ nhật
        area_terms = VGroup()
        for i, rect in enumerate(moved_rects):
            f_x_label = MathTex("f(x)", font_size=28, color=WHITE).move_to(rect)
            dx_label = MathTex("dx", font_size=24, color=WHITE).next_to(rect, DOWN, buff=0.1)
            area_terms.add(VGroup(rect, f_x_label, dx_label))

        # Thêm các dấu cộng giữa các hình chữ nhật
        plus_signs = VGroup()
        for i in range(len(area_terms) - 1):
            plus = MathTex("+", font_size=40).next_to(area_terms[i], RIGHT, buff=0.2)
            plus_signs.add(plus)
        
        # Nhóm tất cả lại để sắp xếp
        full_sum_mobject = VGroup(area_terms[0])
        for i in range(len(plus_signs)):
            full_sum_mobject.add(plus_signs[i], area_terms[i+1])
        
        full_sum_mobject.arrange(RIGHT, buff=0.2).center()
        
        # Thêm "Area =" vào phía trước
        area_text = MathTex("Area =", font_size=40).next_to(full_sum_mobject, LEFT, buff=0.5)
        
        # Nhóm các hình chữ nhật và di chuyển chúng ra giữa màn hình
        self.play(
            FadeOut(graph_group), # Ẩn đồ thị và trục tọa độ
            ReplacementTransform(rects_R4_initial, moved_rects.arrange(RIGHT, buff=0.5).move_to(ORIGIN)),
            Write(area_text)
        )
        self.wait(0.5)
        self.play(
            FadeIn(full_sum_mobject) # Hiện tất cả các thành phần
        )
        self.wait(1)


        # 4 hình chữ nhật này biến thành công thức sigma như hình 2
        formula_sigma_img2 = MathTex(
            r"Area = \sum_{i=1}^{4} f(x_i) \cdot dx", # Đã điều chỉnh n thành i
            font_size=50
        )
        # Di chuyển công thức sigma sang bên phải
        formula_sigma_img2.next_to(graph_group, RIGHT, buff=1.0)

        # Tạo lại các hình chữ nhật để hiển thị cùng đồ thị
        final_rects = axes.get_riemann_rectangles(
            graph, x_range=[0, 1], dx=0.25, 
            input_sample_type="right", color=RED, fill_opacity=0.6
        )

        # Dùng ReplacementTransform để chuyển đổi từ biểu thức tổng sang sigma
        # Đồng thời, cho xuất hiện lại (FadeIn) đồ thị và các hình chữ nhật
        self.play(
            ReplacementTransform(VGroup(area_text, full_sum_mobject), formula_sigma_img2),
            FadeIn(graph_group),
            Create(final_rects)
        )
        self.wait(3)

        # Final cleanup
        self.play(
            FadeOut(formula_sigma_img2),
            FadeOut(title_better_approx),
            FadeOut(graph_group),      # Thêm FadeOut cho đồ thị
            FadeOut(final_rects)       # Thêm FadeOut cho các hình chữ nhật
        )
        self.wait(1)