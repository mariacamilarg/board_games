import dash_bootstrap_components as dbc
import dash_html_components as html

layout = dbc.Navbar(
    [
        dbc.Col(
            dbc.Row(
                html.B(
                    html.A(
                        dbc.NavbarBrand("Web App"),
                        href="/",
                    )
                ),
                justify="center"
            )
        ),
        dbc.Col(
            dbc.Row(
                html.A(
                    dbc.NavbarBrand("Large Screen"),
                    href="/large",
                ),
                justify="center"
            )
        ),
    ],
    color="dark",
    dark=True,
)
