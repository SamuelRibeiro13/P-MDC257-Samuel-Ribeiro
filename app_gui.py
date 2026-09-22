#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA - INTERFACE GRÁFICA MODERNA
Disciplina: Estruturas Matemáticas para Computação
Aluno: Samuel Ribeiro | Matrícula: 2612130058 | Turno: Matutino
=============================================================================
"""

import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Adiciona diretório raiz para importação dos módulos da disciplina
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from P1.atividade_01_conjuntos.conjuntos import (
    processar_conjuntos,
    formatar_conjunto,
    formatar_partes,
)
from P1.atividade_02_divisibilidade.divisibilidade import processar_divisibilidade

# Paleta de Cores Moderna (Deep Slate & Vibrant Accents)
THEME = {
    "bg_app": "#0b0f19",          # Fundo geral ultra-dark
    "bg_surface": "#141c2e",      # Superfície de cards
    "bg_surface_alt": "#1a243a",  # Superfície secundária
    "bg_input": "#1f2b45",        # Fundo dos inputs
    "border": "#2c3b5d",          # Bordas elegantes
    "border_focus": "#6366f1",    # Borda em foco (Indigo)
    "primary": "#4f46e5",         # Indigo vibrante para ação primária
    "primary_hover": "#4338ca",   # Indigo hover
    "secondary": "#253350",       # Botão secundário
    "secondary_hover": "#33456c",
    "text_title": "#ffffff",      # Branco total para títulos
    "text_body": "#e2e8f0",       # Cinza claro para leitura
    "text_muted": "#8d9eb5",      # Cinza azulado para apoios
    "accent_blue": "#38bdf8",     # Ciano
    "accent_indigo": "#818cf8",   # Indigo claro
    "accent_green": "#10b981",    # Verde esmeralda (Sucesso/MDC)
    "accent_amber": "#f59e0b",    # Âmbar (Cardinalidade)
    "accent_rose": "#f43f5e",     # Rosa/Vermelho (Alertas)
    "toast_bg": "#3f121d",        # Fundo do banner de erro
    "toast_border": "#e11d48",    # Borda do banner de erro
}


class ModernApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MathLab • Portfólio de Programação Matemática")
        self.geometry("980x760")
        self.minsize(880, 680)
        self.configure(bg=THEME["bg_app"])

        self.setup_ttk_styles()

        # Layout Principal
        self.create_header()
        self.create_banner_alerta()
        self.create_navigation_bar()

        # Container Central
        self.main_content = tk.Frame(self, bg=THEME["bg_app"])
        self.main_content.pack(fill="both", expand=True, padx=24, pady=(0, 10))

        # Páginas
        self.page_conjuntos = self.build_page_conjuntos(self.main_content)
        self.page_divisibilidade = self.build_page_divisibilidade(self.main_content)

        self.create_footer()

        # Inicializa na aba de conjuntos
        self.switch_tab("conjuntos")

    def setup_ttk_styles(self):
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        # Scrollbar customizada moderna
        self.style.configure(
            "Modern.Vertical.TScrollbar",
            background=THEME["bg_surface_alt"],
            troughcolor=THEME["bg_app"],
            bordercolor=THEME["border"],
            arrowcolor=THEME["text_muted"],
            relief="flat",
        )

    # =========================================================================
    # HEADER & BANNER
    # =========================================================================
    def create_header(self):
        header = tk.Frame(self, bg=THEME["bg_surface"], padx=24, pady=14)
        header.pack(fill="x")

        # Logo / Ícone estético
        icon_box = tk.Label(
            header,
            text="∑",
            font=("Segoe UI", 16, "bold"),
            bg=THEME["primary"],
            fg="#ffffff",
            padx=10,
            pady=2,
        )
        icon_box.pack(side="left", padx=(0, 14))

        # Títulos
        title_box = tk.Frame(header, bg=THEME["bg_surface"])
        title_box.pack(side="left")

        lbl_title = tk.Label(
            title_box,
            text="PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA",
            font=("Segoe UI", 12, "bold"),
            fg=THEME["text_title"],
            bg=THEME["bg_surface"],
        )
        lbl_title.pack(anchor="w")

        lbl_subtitle = tk.Label(
            title_box,
            text="Estruturas Matemáticas para Computação • Profª Cristiane Loesch",
            font=("Segoe UI", 8),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"],
        )
        lbl_subtitle.pack(anchor="w")

        # Chip de Identificação do Aluno
        badge_frame = tk.Frame(header, bg=THEME["bg_input"], padx=12, pady=6)
        badge_frame.pack(side="right")

        dot = tk.Label(
            badge_frame,
            text="●",
            font=("Segoe UI", 9),
            fg=THEME["accent_green"],
            bg=THEME["bg_input"],
        )
        dot.pack(side="left", padx=(0, 6))

        lbl_aluno = tk.Label(
            badge_frame,
            text="Samuel Ribeiro  |  Matrícula: 2612130058  |  Matutino",
            font=("Segoe UI", 9, "bold"),
            fg=THEME["accent_blue"],
            bg=THEME["bg_input"],
        )
        lbl_aluno.pack(side="left")

    def create_banner_alerta(self):
        """Banner de alerta para entradas inválidas (Pegadinha da professora)"""
        self.banner = tk.Frame(
            self,
            bg=THEME["toast_bg"],
            highlightbackground=THEME["toast_border"],
            highlightthickness=1,
            padx=16,
            pady=10,
        )

        self.lbl_banner_icon = tk.Label(
            self.banner,
            text="⚠️",
            font=("Segoe UI", 12),
            bg=THEME["toast_bg"],
            fg=THEME["accent_rose"],
        )
        self.lbl_banner_icon.pack(side="left", padx=(0, 10))

        self.lbl_banner_msg = tk.Label(
            self.banner,
            text="Hoje não Cristiane tenta outra coisa.",
            font=("Segoe UI", 10, "bold"),
            bg=THEME["toast_bg"],
            fg="#ffe4e6",
        )
        self.lbl_banner_msg.pack(side="left")

        btn_close_banner = tk.Button(
            self.banner,
            text="✕",
            font=("Segoe UI", 9, "bold"),
            bg=THEME["toast_bg"],
            fg="#ffe4e6",
            activebackground=THEME["toast_bg"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            bd=0,
            command=self.ocultar_alerta,
        )
        btn_close_banner.pack(side="right")

    def mostrar_alerta(self):
        self.banner.pack(fill="x", padx=24, pady=(10, 0), before=self.main_content)
        # Oculta automaticamente após 5 segundos
        self.after(5000, self.ocultar_alerta)

    def ocultar_alerta(self):
        self.banner.pack_forget()

    # =========================================================================
    # BARRA DE NAVEGAÇÃO
    # =========================================================================
    def create_navigation_bar(self):
        nav_container = tk.Frame(self, bg=THEME["bg_app"], pady=12)
        nav_container.pack(fill="x", padx=24)

        pill_frame = tk.Frame(nav_container, bg=THEME["bg_surface"], padx=4, pady=4)
        pill_frame.pack(side="left")

        self.btn_nav_conj = tk.Button(
            pill_frame,
            text="⊞  Atividade 1 : Teoria dos Conjuntos",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=16,
            pady=7,
            bd=0,
            command=lambda: self.switch_tab("conjuntos"),
        )
        self.btn_nav_conj.pack(side="left", padx=2)

        self.btn_nav_div = tk.Button(
            pill_frame,
            text="÷  Atividade 2 : Divisibilidade, MDC e MMC",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=16,
            pady=7,
            bd=0,
            command=lambda: self.switch_tab("divisibilidade"),
        )
        self.btn_nav_div.pack(side="left", padx=2)

    def switch_tab(self, tab):
        self.page_conjuntos.pack_forget()
        self.page_divisibilidade.pack_forget()
        self.ocultar_alerta()

        if tab == "conjuntos":
            self.btn_nav_conj.configure(
                bg=THEME["primary"],
                fg="#ffffff",
                activebackground=THEME["primary_hover"],
                activeforeground="#ffffff",
            )
            self.btn_nav_div.configure(
                bg=THEME["bg_surface"],
                fg=THEME["text_muted"],
                activebackground=THEME["bg_surface_alt"],
                activeforeground="#ffffff",
            )
            self.page_conjuntos.pack(fill="both", expand=True)
            self.set_status("Módulo de Conjuntos ativo")
        else:
            self.btn_nav_div.configure(
                bg=THEME["primary"],
                fg="#ffffff",
                activebackground=THEME["primary_hover"],
                activeforeground="#ffffff",
            )
            self.btn_nav_conj.configure(
                bg=THEME["bg_surface"],
                fg=THEME["text_muted"],
                activebackground=THEME["bg_surface_alt"],
                activeforeground="#ffffff",
            )
            self.page_divisibilidade.pack(fill="both", expand=True)
            self.set_status("Módulo de Divisibilidade, MDC e MMC ativo")

    # =========================================================================
    # ABA 1: TEORIA DOS CONJUNTOS
    # =========================================================================
    def build_page_conjuntos(self, parent):
        container = tk.Frame(parent, bg=THEME["bg_app"])

        # Card de Inputs
        card_input = tk.Frame(
            container,
            bg=THEME["bg_surface"],
            highlightbackground=THEME["border"],
            highlightthickness=1,
            padx=20,
            pady=16,
        )
        card_input.pack(fill="x", pady=(0, 14))

        # Validador em tempo real (apenas números, espaços, vírgulas e menos)
        vcmd_conj = (self.register(self.filtro_conjunto), "%P")

        # Campo Conjunto A
        box_a = tk.Frame(card_input, bg=THEME["bg_surface"])
        box_a.grid(row=0, column=0, sticky="ew", padx=(0, 12))

        tk.Label(
            box_a,
            text="Conjunto A (elementos separados por espaço)",
            font=("Segoe UI", 9, "bold"),
            fg=THEME["accent_blue"],
            bg=THEME["bg_surface"],
        ).pack(anchor="w", pady=(0, 6))

        self.entry_a = tk.Entry(
            box_a,
            font=("Consolas", 11),
            bg=THEME["bg_input"],
            fg=THEME["text_title"],
            insertbackground="#ffffff",
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["border"],
            highlightcolor=THEME["border_focus"],
            validate="key",
            validatecommand=vcmd_conj,
        )
        self.entry_a.pack(fill="x", ipady=7)
        self.entry_a.insert(0, "1 2 3 4")

        # Campo Conjunto B
        box_b = tk.Frame(card_input, bg=THEME["bg_surface"])
        box_b.grid(row=0, column=1, sticky="ew", padx=(12, 0))

        tk.Label(
            box_b,
            text="Conjunto B (elementos separados por espaço)",
            font=("Segoe UI", 9, "bold"),
            fg=THEME["accent_indigo"],
            bg=THEME["bg_surface"],
        ).pack(anchor="w", pady=(0, 6))

        self.entry_b = tk.Entry(
            box_b,
            font=("Consolas", 11),
            bg=THEME["bg_input"],
            fg=THEME["text_title"],
            insertbackground="#ffffff",
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["border"],
            highlightcolor=THEME["border_focus"],
            validate="key",
            validatecommand=vcmd_conj,
        )
        self.entry_b.pack(fill="x", ipady=7)
        self.entry_b.insert(0, "3 4 5 6")

        card_input.columnconfigure(0, weight=1)
        card_input.columnconfigure(1, weight=1)

        # Botões de Ação
        btn_bar = tk.Frame(card_input, bg=THEME["bg_surface"])
        btn_bar.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(14, 0))

        btn_sample = tk.Button(
            btn_bar,
            text="Carregar Exemplo",
            font=("Segoe UI", 8),
            bg=THEME["secondary"],
            fg=THEME["text_muted"],
            activebackground=THEME["secondary_hover"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=5,
            command=lambda: self.preencher_amostra_conjuntos("1 2 3 4", "3 4 5 6"),
        )
        btn_sample.pack(side="left")

        btn_limpar = tk.Button(
            btn_bar,
            text="Limpar",
            font=("Segoe UI", 9),
            bg=THEME["secondary"],
            fg=THEME["text_body"],
            activebackground=THEME["secondary_hover"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=14,
            pady=6,
            command=self.limpar_conjuntos,
        )
        btn_limpar.pack(side="right", padx=(8, 0))

        btn_calc = tk.Button(
            btn_bar,
            text="⚡ Calcular Operações",
            font=("Segoe UI", 9, "bold"),
            bg=THEME["primary"],
            fg="#ffffff",
            activebackground=THEME["primary_hover"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=6,
            command=self.calcular_conjuntos,
        )
        btn_calc.pack(side="right")

        # Cards Métricos Rápidos
        self.frame_metricas_conj = tk.Frame(container, bg=THEME["bg_app"])
        self.frame_metricas_conj.pack(fill="x", pady=(0, 12))

        self.card_card_a = self.criar_card_metrico(self.frame_metricas_conj, "| A |", "-", THEME["accent_blue"])
        self.card_card_b = self.criar_card_metrico(self.frame_metricas_conj, "| B |", "-", THEME["accent_indigo"])
        self.card_card_uniao = self.criar_card_metrico(self.frame_metricas_conj, "| A ∪ B |", "-", THEME["accent_amber"])
        self.card_card_inter = self.criar_card_metrico(self.frame_metricas_conj, "| A ∩ B |", "-", THEME["accent_green"])
        self.card_inclusao = self.criar_card_metrico(self.frame_metricas_conj, "A ⊆ B", "-", THEME["text_title"])

        # Card de Saída Formatada
        card_out = tk.Frame(
            container,
            bg=THEME["bg_surface"],
            highlightbackground=THEME["border"],
            highlightthickness=1,
            padx=18,
            pady=14,
        )
        card_out.pack(fill="both", expand=True)

        header_out = tk.Frame(card_out, bg=THEME["bg_surface"])
        header_out.pack(fill="x", pady=(0, 8))

        tk.Label(
            header_out,
            text="Detalhamento Matemático Completo",
            font=("Segoe UI", 10, "bold"),
            fg=THEME["text_title"],
            bg=THEME["bg_surface"],
        ).pack(side="left")

        btn_copy = tk.Button(
            header_out,
            text="📋 Copiar Resultados",
            font=("Segoe UI", 8),
            bg=THEME["bg_input"],
            fg=THEME["accent_blue"],
            activebackground=THEME["secondary"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=3,
            command=lambda: self.copiar_texto(self.txt_out_conj),
        )
        btn_copy.pack(side="right")

        scroll = ttk.Scrollbar(card_out, orient="vertical", style="Modern.Vertical.TScrollbar")
        scroll.pack(side="right", fill="y")

        self.txt_out_conj = tk.Text(
            card_out,
            font=("Consolas", 10),
            bg=THEME["bg_input"],
            fg=THEME["text_body"],
            insertbackground="#ffffff",
            relief="flat",
            wrap="word",
            yscrollcommand=scroll.set,
            padx=12,
            pady=10,
        )
        self.txt_out_conj.pack(fill="both", expand=True)
        scroll.config(command=self.txt_out_conj.yview)

        # Configuração de tags de destaque de sintaxe
        self.txt_out_conj.tag_configure("header", font=("Segoe UI", 10, "bold"), foreground=THEME["accent_indigo"])
        self.txt_out_conj.tag_configure("accent", font=("Consolas", 10, "bold"), foreground=THEME["accent_blue"])
        self.txt_out_conj.tag_configure("math", font=("Consolas", 10), foreground="#ffffff")
        self.txt_out_conj.tag_configure("sub", font=("Consolas", 9), foreground=THEME["text_muted"])

        return container

    def criar_card_metrico(self, parent, label_text, initial_val, color_accent):
        card = tk.Frame(
            parent,
            bg=THEME["bg_surface"],
            highlightbackground=THEME["border"],
            highlightthickness=1,
            padx=12,
            pady=8,
        )
        card.pack(side="left", fill="x", expand=True, padx=4)

        lbl_desc = tk.Label(
            card,
            text=label_text,
            font=("Segoe UI", 8, "bold"),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"],
        )
        lbl_desc.pack(anchor="w")

        lbl_val = tk.Label(
            card,
            text=initial_val,
            font=("Segoe UI", 13, "bold"),
            fg=color_accent,
            bg=THEME["bg_surface"],
        )
        lbl_val.pack(anchor="w", pady=(2, 0))

        return lbl_val

    def filtro_conjunto(self, texto):
        permitidos = "0123456789 ,-"
        for c in texto:
            if c not in permitidos:
                return False
        return True

    def preencher_amostra_conjuntos(self, a, b):
        self.entry_a.delete(0, tk.END)
        self.entry_a.insert(0, a)
        self.entry_b.delete(0, tk.END)
        self.entry_b.insert(0, b)

    def limpar_conjuntos(self):
        self.entry_a.delete(0, tk.END)
        self.entry_b.delete(0, tk.END)
        self.txt_out_conj.delete("1.0", tk.END)
        self.card_card_a.config(text="-")
        self.card_card_b.config(text="-")
        self.card_card_uniao.config(text="-")
        self.card_card_inter.config(text="-")
        self.card_inclusao.config(text="-")
        self.ocultar_alerta()
        self.set_status("Campos limpos.")

    def calcular_conjuntos(self):
        txt_a = self.entry_a.get().strip()
        txt_b = self.entry_b.get().strip()

        try:
            tokens_a = txt_a.replace(",", " ").split()
            tokens_b = txt_b.replace(",", " ").split()
            if not tokens_a or not tokens_b:
                raise ValueError("Vazio")

            A = []
            for t in tokens_a:
                v = int(t)
                if v not in A:
                    A.append(v)

            B = []
            for t in tokens_b:
                v = int(t)
                if v not in B:
                    B.append(v)
        except Exception:
            self.mostrar_alerta()
            self.set_status("Entrada inválida detectada.", erro=True)
            return

        self.ocultar_alerta()
        res = processar_conjuntos(A, B)

        # Atualiza métricas rápidas
        self.card_card_a.config(text=str(res["card_A"]))
        self.card_card_b.config(text=str(res["card_B"]))
        self.card_card_uniao.config(text=str(res["card_uniao"]))
        self.card_card_inter.config(text=str(res["card_intersecao"]))
        self.card_inclusao.config(
            text="Sim" if res["A_sub_B"] else "Não",
            fg=THEME["accent_green"] if res["A_sub_B"] else THEME["accent_rose"],
        )

        # Detalhamento no Text
        self.txt_out_conj.delete("1.0", tk.END)

        self.txt_out_conj.insert(tk.END, "CONJUNTOS FORNECIDOS\n", "header")
        self.txt_out_conj.insert(tk.END, f"A = {formatar_conjunto(A)}\n", "accent")
        self.txt_out_conj.insert(tk.END, f"B = {formatar_conjunto(B)}\n\n", "accent")

        self.txt_out_conj.insert(tk.END, "1. UNIÃO (A ∪ B)\n", "header")
        self.txt_out_conj.insert(tk.END, f"{formatar_conjunto(res['uniao'])}\n\n", "math")

        self.txt_out_conj.insert(tk.END, "2. INTERSEÇÃO (A ∩ B)\n", "header")
        self.txt_out_conj.insert(tk.END, f"{formatar_conjunto(res['intersecao'])}\n\n", "math")

        self.txt_out_conj.insert(tk.END, "3. DIFERENÇAS\n", "header")
        self.txt_out_conj.insert(tk.END, f"A - B = {formatar_conjunto(res['dif_A_B'])}\n", "math")
        self.txt_out_conj.insert(tk.END, f"B - A = {formatar_conjunto(res['dif_B_A'])}\n\n", "math")

        self.txt_out_conj.insert(tk.END, "4. CONJUNTO DAS PARTES\n", "header")
        self.txt_out_conj.insert(tk.END, f"P(A) = {formatar_partes(res['partes_A'])}\n", "sub")
        self.txt_out_conj.insert(tk.END, f"Cardinalidade |P(A)|: {res['card_partes_A']} (2^{res['card_A']})\n\n", "math")
        self.txt_out_conj.insert(tk.END, f"P(B) = {formatar_partes(res['partes_B'])}\n", "sub")
        self.txt_out_conj.insert(tk.END, f"Cardinalidade |P(B)|: {res['card_partes_B']} (2^{res['card_B']})\n\n", "math")

        self.txt_out_conj.insert(tk.END, "5. PARTIÇÃO DE A\n", "header")
        if res["particao_A"]:
            p_formatada = [formatar_conjunto(p) for p in res["particao_A"]]
            self.txt_out_conj.insert(tk.END, f"P = {{{', '.join(p_formatada)}}}\n\n", "math")
        else:
            self.txt_out_conj.insert(tk.END, "Conjunto vazio, sem partição.\n\n", "sub")

        self.txt_out_conj.insert(tk.END, "6. PRODUTO CARTESIANO (A × B)\n", "header")
        pares_str = ", ".join(f"({a}, {b})" for a, b in res["prod_cartesiano"])
        self.txt_out_conj.insert(tk.END, f"{{{pares_str}}}\n", "sub")
        self.txt_out_conj.insert(tk.END, f"Total de elementos: {len(res['prod_cartesiano'])} pares\n\n", "math")

        self.txt_out_conj.insert(tk.END, "7. RELAÇÕES DE INCLUSÃO\n", "header")
        self.txt_out_conj.insert(tk.END, f"A ⊆ B: {'Sim (contido)' if res['A_sub_B'] else 'Não está contido'}\n", "math")
        self.txt_out_conj.insert(tk.END, f"B ⊆ A: {'Sim (contido)' if res['B_sub_A'] else 'Não está contido'}\n", "math")

        self.set_status(f"Operações calculadas com sucesso (|A|={len(A)}, |B|={len(B)})")

    # =========================================================================
    # ABA 2: DIVISIBILIDADE, MDC E MMC
    # =========================================================================
    def build_page_divisibilidade(self, parent):
        container = tk.Frame(parent, bg=THEME["bg_app"])

        # Card de Inputs
        card_input = tk.Frame(
            container,
            bg=THEME["bg_surface"],
            highlightbackground=THEME["border"],
            highlightthickness=1,
            padx=20,
            pady=16,
        )
        card_input.pack(fill="x", pady=(0, 14))

        vcmd_digits = (self.register(self.filtro_digitos), "%P")

        # Campo Número A
        box_a = tk.Frame(card_input, bg=THEME["bg_surface"])
        box_a.grid(row=0, column=0, sticky="ew", padx=(0, 12))

        tk.Label(
            box_a,
            text="Primeiro Número Inteiro (a)",
            font=("Segoe UI", 9, "bold"),
            fg=THEME["accent_blue"],
            bg=THEME["bg_surface"],
        ).pack(anchor="w", pady=(0, 6))

        self.entry_div_a = tk.Entry(
            box_a,
            font=("Consolas", 11),
            bg=THEME["bg_input"],
            fg=THEME["text_title"],
            insertbackground="#ffffff",
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["border"],
            highlightcolor=THEME["border_focus"],
            validate="key",
            validatecommand=vcmd_digits,
        )
        self.entry_div_a.pack(fill="x", ipady=7)
        self.entry_div_a.insert(0, "48")

        # Campo Número B
        box_b = tk.Frame(card_input, bg=THEME["bg_surface"])
        box_b.grid(row=0, column=1, sticky="ew", padx=(12, 0))

        tk.Label(
            box_b,
            text="Segundo Número Inteiro (b)",
            font=("Segoe UI", 9, "bold"),
            fg=THEME["accent_indigo"],
            bg=THEME["bg_surface"],
        ).pack(anchor="w", pady=(0, 6))

        self.entry_div_b = tk.Entry(
            box_b,
            font=("Consolas", 11),
            bg=THEME["bg_input"],
            fg=THEME["text_title"],
            insertbackground="#ffffff",
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["border"],
            highlightcolor=THEME["border_focus"],
            validate="key",
            validatecommand=vcmd_digits,
        )
        self.entry_div_b.pack(fill="x", ipady=7)
        self.entry_div_b.insert(0, "18")

        card_input.columnconfigure(0, weight=1)
        card_input.columnconfigure(1, weight=1)

        # Botões de Ação
        btn_bar = tk.Frame(card_input, bg=THEME["bg_surface"])
        btn_bar.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(14, 0))

        btn_sample = tk.Button(
            btn_bar,
            text="Testar 48 e 18",
            font=("Segoe UI", 8),
            bg=THEME["secondary"],
            fg=THEME["text_muted"],
            activebackground=THEME["secondary_hover"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=5,
            command=lambda: self.preencher_amostra_div("48", "18"),
        )
        btn_sample.pack(side="left")

        btn_sample_primos = tk.Button(
            btn_bar,
            text="Testar Primos (35 e 12)",
            font=("Segoe UI", 8),
            bg=THEME["secondary"],
            fg=THEME["text_muted"],
            activebackground=THEME["secondary_hover"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=5,
            command=lambda: self.preencher_amostra_div("35", "12"),
        )
        btn_sample_primos.pack(side="left", padx=(8, 0))

        btn_limpar = tk.Button(
            btn_bar,
            text="Limpar",
            font=("Segoe UI", 9),
            bg=THEME["secondary"],
            fg=THEME["text_body"],
            activebackground=THEME["secondary_hover"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=14,
            pady=6,
            command=self.limpar_divisibilidade,
        )
        btn_limpar.pack(side="right", padx=(8, 0))

        btn_calc = tk.Button(
            btn_bar,
            text="⚡ Executar Algoritmo de Euclides",
            font=("Segoe UI", 9, "bold"),
            bg=THEME["primary"],
            fg="#ffffff",
            activebackground=THEME["primary_hover"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=6,
            command=self.calcular_divisibilidade,
        )
        btn_calc.pack(side="right")

        # Cards Métricos Rápidos
        self.frame_metricas_div = tk.Frame(container, bg=THEME["bg_app"])
        self.frame_metricas_div.pack(fill="x", pady=(0, 12))

        self.card_div = self.criar_card_metrico(self.frame_metricas_div, "DIV (a // b)", "-", THEME["text_body"])
        self.card_mod = self.criar_card_metrico(self.frame_metricas_div, "MOD (a % b)", "-", THEME["accent_amber"])
        self.card_mdc = self.criar_card_metrico(self.frame_metricas_div, "MDC(a, b)", "-", THEME["accent_green"])
        self.card_mmc = self.criar_card_metrico(self.frame_metricas_div, "MMC(a, b)", "-", THEME["accent_blue"])

        # Card de Saída Formatada
        card_out = tk.Frame(
            container,
            bg=THEME["bg_surface"],
            highlightbackground=THEME["border"],
            highlightthickness=1,
            padx=18,
            pady=14,
        )
        card_out.pack(fill="both", expand=True)

        header_out = tk.Frame(card_out, bg=THEME["bg_surface"])
        header_out.pack(fill="x", pady=(0, 8))

        tk.Label(
            header_out,
            text="Passo a Passo do Algoritmo de Euclides & Dedução do MMC",
            font=("Segoe UI", 10, "bold"),
            fg=THEME["text_title"],
            bg=THEME["bg_surface"],
        ).pack(side="left")

        btn_copy = tk.Button(
            header_out,
            text="📋 Copiar Resultados",
            font=("Segoe UI", 8),
            bg=THEME["bg_input"],
            fg=THEME["accent_blue"],
            activebackground=THEME["secondary"],
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=3,
            command=lambda: self.copiar_texto(self.txt_out_div),
        )
        btn_copy.pack(side="right")

        scroll = ttk.Scrollbar(card_out, orient="vertical", style="Modern.Vertical.TScrollbar")
        scroll.pack(side="right", fill="y")

        self.txt_out_div = tk.Text(
            card_out,
            font=("Consolas", 10),
            bg=THEME["bg_input"],
            fg=THEME["text_body"],
            insertbackground="#ffffff",
            relief="flat",
            wrap="word",
            yscrollcommand=scroll.set,
            padx=12,
            pady=10,
        )
        self.txt_out_div.pack(fill="both", expand=True)
        scroll.config(command=self.txt_out_div.yview)

        self.txt_out_div.tag_configure("header", font=("Segoe UI", 10, "bold"), foreground=THEME["accent_indigo"])
        self.txt_out_div.tag_configure("step", font=("Consolas", 10, "bold"), foreground=THEME["accent_blue"])
        self.txt_out_div.tag_configure("result", font=("Consolas", 11, "bold"), foreground=THEME["accent_green"])
        self.txt_out_div.tag_configure("sub", font=("Consolas", 9), foreground=THEME["text_muted"])

        return container

    def filtro_digitos(self, texto):
        if texto == "":
            return True
        return texto.isdigit()

    def preencher_amostra_div(self, a, b):
        self.entry_div_a.delete(0, tk.END)
        self.entry_div_a.insert(0, a)
        self.entry_div_b.delete(0, tk.END)
        self.entry_div_b.insert(0, b)

    def limpar_divisibilidade(self):
        self.entry_div_a.delete(0, tk.END)
        self.entry_div_b.delete(0, tk.END)
        self.txt_out_div.delete("1.0", tk.END)
        self.card_div.config(text="-")
        self.card_mod.config(text="-")
        self.card_mdc.config(text="-")
        self.card_mmc.config(text="-")
        self.ocultar_alerta()
        self.set_status("Campos limpos.")

    def calcular_divisibilidade(self):
        txt_a = self.entry_div_a.get().strip()
        txt_b = self.entry_div_b.get().strip()

        try:
            val_a = int(txt_a)
            val_b = int(txt_b)
            if val_a <= 0 or val_b <= 0:
                raise ValueError("Deve ser > 0")
        except Exception:
            self.mostrar_alerta()
            self.set_status("Entrada inválida. Digite inteiros positivos.", erro=True)
            return

        self.ocultar_alerta()
        res = processar_divisibilidade(val_a, val_b)

        # Atualiza cards métricos
        self.card_div.config(text=str(res["div"]))
        self.card_mod.config(text=str(res["mod"]))
        self.card_mdc.config(text=str(res["mdc"]))
        self.card_mmc.config(text=str(res["mmc"]))

        # Atualiza texto de procedimentos
        self.txt_out_div.delete("1.0", tk.END)

        self.txt_out_div.insert(tk.END, "DIVISÃO EUCLIDIANA INICIAL\n", "header")
        self.txt_out_div.insert(
            tk.END,
            f"{val_a} // {val_b} = {res['div']} (DIV)\n"
            f"{val_a} % {val_b}  = {res['mod']} (MOD)\n"
            f"Equação: {val_a} = {val_b} × {res['div']} + {res['mod']}\n\n",
            "step",
        )

        self.txt_out_div.insert(tk.END, "PASSOS DO ALGORITMO DE EUCLIDES (Divisões Sucessivas)\n", "header")
        for i, (dividendo, divisor, q, r) in enumerate(res["passos"], 1):
            self.txt_out_div.insert(
                tk.END,
                f"Passo {i}:  {dividendo:>6} = {divisor:>6} × {q:>4} + {r:>6}\n",
                "step",
            )

        self.txt_out_div.insert(
            tk.END,
            f"\n→ Maior Divisor Comum: MDC({val_a}, {val_b}) = {res['mdc']}\n\n",
            "result",
        )

        self.txt_out_div.insert(tk.END, "CÁLCULO DO MMC PELA RELAÇÃO FUNDAMENTAL\n", "header")
        self.txt_out_div.insert(
            tk.END,
            "Propriedade: MDC(a, b) × MMC(a, b) = a × b\n"
            f"Fórmula:     MMC({val_a}, {val_b}) = ({val_a} × {val_b}) // {res['mdc']}\n",
            "sub",
        )
        self.txt_out_div.insert(
            tk.END,
            f"→ Resultado: MMC({val_a}, {val_b}) = {res['mmc']}\n",
            "result",
        )

        self.set_status(f"Euclides executado: MDC = {res['mdc']} | MMC = {res['mmc']}")

    # =========================================================================
    # UTILITÁRIOS E FOOTER
    # =========================================================================
    def copiar_texto(self, widget):
        conteudo = widget.get("1.0", tk.END).strip()
        if conteudo:
            self.clipboard_clear()
            self.clipboard_append(conteudo)
            self.set_status("✓ Resultados copiados para a área de transferência!")
        else:
            self.set_status("Nenhum resultado para copiar.", erro=True)

    def create_footer(self):
        footer = tk.Frame(self, bg=THEME["bg_surface"], padx=24, pady=8)
        footer.pack(fill="x", side="bottom")

        self.lbl_status = tk.Label(
            footer,
            text="Pronto para uso",
            font=("Segoe UI", 9),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"],
        )
        self.lbl_status.pack(side="left")

        lbl_version = tk.Label(
            footer,
            text="Portfólio P1 • EMC 2026-2",
            font=("Segoe UI", 8),
            fg=THEME["text_muted"],
            bg=THEME["bg_surface"],
        )
        lbl_version.pack(side="right")

    def set_status(self, msg, erro=False):
        cor = THEME["accent_rose"] if erro else THEME["accent_green"]
        self.lbl_status.config(text=msg, fg=cor)


def main():
    app = ModernApp()
    app.mainloop()


if __name__ == "__main__":
    main()
