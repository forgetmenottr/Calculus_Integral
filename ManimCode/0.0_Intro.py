from manim import *

class CalculusProjectIntro(Scene):
    def construct(self):
        # --- COLOR ---
        primary_color = BLUE
        secondary_color = TEAL
        
        # --- PROJECT TITLE ---
        title = MarkupText(
            "CALCULUS PROJECT", 
            font_size=72, 
            weight=BOLD,
            gradient=(primary_color, secondary_color)
        )
        
        subtitle = Text(
            "A project by students of",
            font_size=32,
            line_spacing=1
        )
        subtitle.next_to(title, DOWN, buff=0.5)
        
        subtitle2 = Text(
            "Ho Chi Minh City University of Technology",
            font_size=32,
            line_spacing=1
        )
        subtitle2.next_to(title, DOWN, buff=1)
        
        # Grouping
        group_scene1 = VGroup(title, subtitle,subtitle2).center()
        
        # Animation_1
        self.play(Write(title), run_time=1)
        self.play(
            Write(subtitle, shift=UP),
            Write(subtitle2, shift=UP)
            )
        self.wait(1)
        self.play(FadeOut(group_scene1, shift=UP))

        # --- GROUP INFORMATION AND INSTRUCTOR ---
        
        group_info = MarkupText(
            f"Conducted by <span fgcolor='{TEAL_A}'>Group CA05</span>", 
            font_size=40
        )
        
        instructor_info = MarkupText(
            f"Instructor: <span fgcolor='{TEAL_A}'>Prof. Truong Van Tri</span>", 
            font_size=30
        )
        
        group_scene2 = VGroup(group_info, instructor_info).arrange(DOWN, buff=0.8)
        
        line = Line(LEFT, RIGHT, color=GREY_B).scale(3)
        line.next_to(group_info, DOWN, buff=0.4)
        instructor_info.next_to(line, DOWN, buff=0.4)
        
        # Animation_2
        self.play(GrowFromCenter(group_info))
        self.play(Create(line))
        self.play(Write(instructor_info))
        self.wait(1)
        self.play(FadeOut(group_info), Uncreate(line), FadeOut(instructor_info))

        # --- TOPIC ---
        
        # Highlight color
        hl_color = TEAL_A  
        
        # 2. Topic
        topic_str1 = Text("Definite and Indefinite Integral")
        topic_str2 = Text("Theory and Applications")
        
        # Tiêu đề nhỏ phía trên
        header_text = "TOPIC" 
        header_topic = Text(header_text, font_size=60, weight=BOLD, color=BLUE)
        header_topic.to_edge(UP, buff=1.5)
        
        topic_content = VGroup(
            topic_str1,
            topic_str2
        )
        
        topic_content.arrange(DOWN, buff=topic_str1.height * 0.2) 
        topic_content.center()
        
        
        # Animation
        self.play(FadeIn(header_topic, shift=DOWN))
        self.play(Write(topic_content),run_time = 8)
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))