while True:
    file = input()
    extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
    i = file.rfind('.')
    for f in extensions:
        if f == file[i+1:]:
            print(f)
            a = 1;
            break
    if a != 1:
        extensions.append(file[i+1:])            #если расширения нет, то печатаем его
    print(file[i+1:])