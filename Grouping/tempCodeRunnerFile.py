fig = px.bar(data,x=list(set(df[group])),y=num_col,barmode='group',labels={'x':str(group)})
        # fig.write_image(my_path+'group'+group+'.png')