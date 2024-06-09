def get_file_path(file_extension) -> str:
    textFilesPath = "/Documents/Text Files/"
    spreadSheetsPath = "/Documents/Spreadsheets/"
    presentationsPath = "/Documents/Presentations/"
    pdfPath = "/Documents/PDFs/"
    staticImagesPath = "/Images/Static/"
    gifsPath = "/Images/GIFs/"
    vectorsPath = "/Images/SVGs/"
    audioPath = "/Audio/"
    videosPath = "/Videos/"
    archivesPath = "/Archives/"
    programmingPath = "/Code/Programming/"
    markupPath = "/Code/Markup/"
    executablesPath = "/Executables/"
    miscPath = "/Miscellaneous/"
    othersPath = "/Miscellaneous/Other/"
    
    file_formats = {
            "txt": textFilesPath, 
            "doc": textFilesPath, 
            "docx": textFilesPath,
            "xls": spreadSheetsPath,
            "xlsx": spreadSheetsPath,
            "ppt": presentationsPath,
            "pptx": presentationsPath,
            "pdf": pdfPath,
            "jpg": staticImagesPath,
            "jpeg": staticImagesPath,
            "png": staticImagesPath,
            "gif": gifsPath,
            "svg": vectorsPath,
            "eps": vectorsPath,
            "wav": audioPath,
            "aiff": audioPath,
            "mp3": audioPath,
            "aac": audioPath,
            "flac": audioPath,
            "alac": audioPath,
            "avi": videosPath,
            "mp4": videosPath,
            "mkv": videosPath,
            "mov": videosPath,
            "zip": archivesPath,
            "rar": archivesPath,
            "7z": archivesPath,
            "tar": archivesPath,
            "py": programmingPath,
            "js": programmingPath,
            "java": programmingPath,
            "cpp": programmingPath,
            "rb": programmingPath,
            "html": markupPath,
            "xml": markupPath,
            "json": markupPath,
            "exe": executablesPath,
            "dmg": executablesPath,
            "app": executablesPath,
            "mdb": miscPath,
            "sql": miscPath,
            "ttf": miscPath,
            "otf": miscPath,
            "jar": miscPath,
    }

    return file_formats.get(file_extension, othersPath)
