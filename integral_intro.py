from manim import *

# Scene 1: Giới thiệu hàm số và miền tích phân
class IntroScene(Scene):
    def construct(self):
        # 1️⃣ Tạo hệ trục toạ độ
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=4,
            axis_config={"color": GREY_B},
            tips=False
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))
        self.wait(0.5)

        # 2️⃣ Định nghĩa hàm số (ví dụ f(x) = x^2)
        def func(x):
            return x**2

        # 3️⃣ Vẽ đồ thị hàm f(x)
        graph = axes.plot(func, x_range=[0, 3], color=BLUE)
        graph_label = axes.get_graph_label(graph, label="f(x)=x^2", x_val=2.8, direction=UP+RIGHT)

        # Animation vẽ đường cong từ từ
        self.play(Create(graph, run_time=2))
        self.play(Write(graph_label))
        self.wait(0.5)

        # 4️⃣ Đánh dấu đoạn [a,b]
        a = 0
        b = 3
        line_a = axes.get_vertical_line(axes.c2p(a, func(a)), color=YELLOW)
        line_b = axes.get_vertical_line(axes.c2p(b, func(b)), color=YELLOW)
        label_a = MathTex("a").next_to(axes.c2p(a, 0), DOWN)
        label_b = MathTex("b").next_to(axes.c2p(b, 0), DOWN)

        self.play(Create(line_a), Create(line_b), Write(label_a), Write(label_b))
        self.wait(0.5)

        # 5️⃣ Tô màu vùng dưới đường cong giữa a và b
        area = axes.get_area(graph, x_range=[a, b], color=BLUE, opacity=0.3)
        self.play(FadeIn(area))
        self.wait(1)

        # 6️⃣ Thêm dòng chữ mô tả
        text = Tex(
            "Tìm diện tích phần mặt phẳng giới hạn bởi đồ thị $f(x)$,\\\n"
            "trục hoành và các đường thẳng $x=a$, $x=b$.",
            font_size=30
        )
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(2)