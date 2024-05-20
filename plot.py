import plotly.express as px


def make_chart(df):
    fig = px.bar(df, x='block_date', y='TTL', color='protocol', 
             title='Restaking TTL',
             labels={'block_date': 'Date', 'value': 'Value', 'symbol': 'Token'},
             hover_data={'block_date': True, 'TTL': ':.2f'}
             )

    # Update layout for a dark theme
    fig.update_layout(
        template='plotly_dark',  # Change template to a dark one
        xaxis_title='Date',
        yaxis_title='ETH',
    )

    return(fig)