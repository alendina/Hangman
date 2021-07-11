st = input()
for i in st:
    if i == i.capitalize():
        st = st.replace(i, '_' + i.lower())
print(st.strip('_'))
