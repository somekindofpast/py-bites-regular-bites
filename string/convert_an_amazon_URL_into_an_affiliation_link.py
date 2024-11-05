def generate_affiliation_link(url: str):
    result = "http://www.amazon.com/dp/"
    for i in range(url.index("/dp/") + 4, len(url)):
        if url[i] == '/':
            break
        result += url[i]
    return result + "/?tag=pyb0f-20"


if __name__ == '__main__':
    print(generate_affiliation_link("https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X"))