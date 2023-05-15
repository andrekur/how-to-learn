
with  open('./styles/style.css', 'r') as file:
    css_selector_prefix = '.'

    bloks = set()

    for line in file:
        if line.startswith(css_selector_prefix):
            line = line[1: len(line)]
            # попали в блок
            blok_name = line.split('__')[0].split(' ')[0].split('_')[0]
            bloks.add(blok_name)
    
    file.seek(0)

    bloks_modif = { blok:[] for blok in bloks}
    bloks_elem = { blok:[] for blok in bloks}

    for line in file:
        if line.startswith(css_selector_prefix):
            line = line[1: len(line)]
            full_class_name = line.split(' ')[0]
            blok_name = line.split('__')[0].split(' ')[0].split('_')[0]
            if '__' in full_class_name:
                bloks_elem[blok_name].append(full_class_name)
            elif '_' in full_class_name:
                bloks_modif[blok_name].append(full_class_name)
    
    print('модификаторы', bloks_modif, '\n')
    print('блоки', bloks_elem)

    import os

    project_path = os.getcwd()
    main_path = os.path.join(project_path, 'bloks')
    os.mkdir(main_path)
    for blok in bloks:
        blok_path = os.path.join(main_path, blok)
        print(blok_path)
        os.mkdir(blok_path)
        open(f'{blok_path}/{blok}.css', "w")
        # create elem
        elem_names = bloks_elem.get(blok)
        for elem_name in elem_names:
            name = elem_name.replace(blok, '')
            _path = os.path.join(blok_path, name)
            os.mkdir(_path)
            open(f'{_path}/{elem_name}.css', "w")
            
        elem_names = bloks_modif.get(blok)
        for elem_name in elem_names:
            print(elem_name)
            name = elem_name.replace(blok, '').split('_')[1]
            name = f'_{name}'
            print(name)
            _path = os.path.join(blok_path, name)
            try:
                os.mkdir(_path)
            except Exception as ex:
                print(ex)
                pass
            
            open(f'{_path}/{elem_name}.css', "w")

                

