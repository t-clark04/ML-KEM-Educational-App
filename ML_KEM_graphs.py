import plotly.graph_objects as go

def draw_square(fig, x0, y0, size, mid_label, upper_label, color, hovertext = "", exact = True):
    fig.add_shape(
    type="rect",
    x0=x0, y0=y0, x1=x0 + size, y1=y0 + size,
    fillcolor= color,
    line=dict(color="black")
    )
    
    fig.add_annotation(
    x=x0 + size/2, y=y0 + size/2,
    text=f"<b>{mid_label}</b>",
    showarrow=False,
    font=dict(size=20)
    )
    
    fig.add_annotation(
    x=x0 + size/2, y=y0 + size + 0.2,
    text=f"{upper_label}",
    showarrow=False,
    font=dict(size=12),
    xanchor="center",
    yanchor="bottom"
    )

    if exact == True:
        text = f"{size} x {size}"
    else:
        text=f"k × k"

    fig.add_annotation(
    x=x0 + size/2, y=y0 - 0.2,
    text = text,
    showarrow=False,
    font=dict(size=12),
    xanchor="center",
    yanchor="top"
    )

    fig.add_trace(go.Scatter(
        x=[x0 + size / 2],
        y=[y0 + size / 2],
        mode="markers",
        marker=dict(
            size=size * 40,   # scale to cover the shape
            color="rgba(0,0,0,0)",
            symbol="square",
        ),
        hovertemplate=f"<b>{mid_label}</b><br>{hovertext}<extra></extra>",
        showlegend=False,
    ))


def draw_rectangle(fig, x0, y0, size, mid_label, upper_label, color, hovertext = ""):
    fig.add_shape(
    type="rect",
    x0=x0, y0=y0, x1=x0 + 1, y1=y0 + size,
    fillcolor= color,
    line=dict(color="black")
    )
    
    fig.add_annotation(
    x=x0 + 0.5, y=y0 + size/2,
    text=f"<b>{mid_label}</b>",
    showarrow=False,
    font=dict(size=20)
    )
    
    fig.add_annotation(
    x=x0 + 0.5, y=y0 + size + 0.2,
    text=f"{upper_label}",
    showarrow=False,
    font=dict(size=12),
    xanchor="center",
    yanchor="bottom"
    )

    fig.add_annotation(
    x=x0 + 0.5, y=y0 - 0.2,
    text=f"k × 1",
    showarrow=False,
    font=dict(size=12),
    xanchor="center",
    yanchor="top"
    )

    fig.add_trace(go.Scatter(
        x=[x0],
        y=[y0 + size / 2],
        mode="markers",
        marker=dict(
            size=size * 40,   # scale to cover the shape
            color="rgba(0,0,0,0)",
            symbol="square",
        ),
        hovertemplate=f"<b>{mid_label}</b><br>{hovertext}<extra></extra>",
        showlegend=False,
    ))

def draw_rectangle_horiz(fig, x0, y0, size, mid_label, upper_label, color, hovertext = ""):
    fig.add_shape(
    type="rect",
    x0=x0, y0=y0, x1=x0 + size, y1=y0 + 1,
    fillcolor= color,
    line=dict(color="black")
    )
    
    fig.add_annotation(
    x=x0 + size/2, y=y0 + 0.5,
    text=f"<b>{mid_label}</b>",
    showarrow=False,
    font=dict(size=20)
    )
    
    fig.add_annotation(
    x=x0 + size/2, y=y0 + 1.2,
    text=f"{upper_label}",
    showarrow=False,
    font=dict(size=12),
    xanchor="center",
    yanchor="bottom"
    )

    fig.add_annotation(
    x=x0 + size/2, y=y0 - 0.2,
    text=f"1 × k",
    showarrow=False,
    font=dict(size=12),
    xanchor="center",
    yanchor="top"
    )

    fig.add_trace(go.Scatter(
        x=[x0 + size / 2],
        y=[y0 + 0.5],
        mode="markers",
        marker=dict(
            size=size * 40,   # scale to cover the shape
            color="rgba(0,0,0,0)",
            symbol="square",
        ),
        hovertemplate=f"<b>{mid_label}</b><br>{hovertext}<extra></extra>",
        showlegend=False,
    ))

def draw_plus(fig, x,y):
    fig.add_annotation(
        x=x, y=y,
        text="+",
        showarrow=False,
        font=dict(size=24),
        xanchor="center",
        yanchor="middle"
    )

def draw_minus(fig, x,y):
    fig.add_annotation(
        x=x, y=y,
        text="-",
        showarrow=False,
        font=dict(size=24),
        xanchor="center",
        yanchor="middle"
    )

def draw_equals(fig, x,y):
    fig.add_annotation(
        x=x, y=y,
        text="=",
        showarrow=False,
        font=dict(size=24),
        xanchor="center",
        yanchor="middle"
    )

def draw_arrow(fig, xhead, xtail, y, label):
    fig.add_annotation(
    x=xhead, y=y,          # arrow head near Bob
    ax=xtail, ay=y,        # arrow tail near Alice
    xref="x", yref="y",
    axref="x", ayref="y",
    text="",
    showarrow=True,
    arrowhead=3,
    arrowsize=1.5,
    arrowwidth=2
    )

    # --- Label above the arrow ---
    fig.add_annotation(
        x=(xhead + xtail)/2, y=y + 0.25,           # midpoint of the arrow, slightly above
        text=f"<b>{label}</b>",
        showarrow=False,
        font=dict(size=12),
        xanchor="center"
    )

def add_header(fig, x,y,label):
    fig.add_annotation(
    x=x, y=y,          # above A block
    text=f"<b><u>{label}</u></b>",
    showarrow=False,
    font=dict(size=18, color="black"),
    xanchor="center",
    yanchor="bottom"
    )

def add_subheader(fig, x,y,label):
    fig.add_annotation(
    x=x, y=y,          # sublabel just below "Alice"
    text=f"<u>{label}</u>",
    showarrow=False,
    font=dict(size=12, color="black"),
    xanchor="center",
    yanchor="bottom"
    )

def draw_approx(fig, x,y):
        fig.add_annotation(
        x=x, y=y,
        text="≈",
        showarrow=False,
        font=dict(size=30),
        xanchor="center",
        yanchor="middle"
    )