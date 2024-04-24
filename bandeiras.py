from PIL import Image, ImageDraw

def bandeira_italia(height):
    width = 3 * height // 2
    GREEN = (34, 139, 34)
    WHITE = (255, 255, 255)
    RED = (239, 65, 53)
    image = Image.new("RGB", (width, height), WHITE)

    offset = width // 3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), GREEN)
            image.putpixel((x + 2 * offset, y), RED)

    return image


def bandeira_brasil(height):
    width = 3 * height // 2
    BLUE = (0, 39, 118)
    GREEN = (0, 156, 59)
    YELLOW = (255, 223, 0)
    
    
    margem = 17 * height // 140
    center = (width // 2, height // 2)
    radius = height // 4

    imagem = Image.new('RGB', (width, height), GREEN)

    for x in range(margem, width - margem):
        for y in range(margem, height - margem):
            if x <= center[0] and y <= center[1] and (center[1] - y) <= 0.64 * (x - margem):
                imagem.putpixel((x,y), YELLOW)
            if x > center[0] and y <= center[1] and (center[1] - y) <= -0.64 * (x - center[0]) + center[1] - margem:
                imagem.putpixel((x,y), YELLOW)
            if x <= center[0] and y > center[1] and (y - center[1]) <= 0.64 * (x - margem):
                imagem.putpixel((x,y), YELLOW)
            if x > center[0] and y > center[1] and (y - center[1]) <= -0.64 * (x - center[0]) + center[1] - margem:
                imagem.putpixel((x,y), YELLOW)
    
    for x in range(center[0] - radius, center[0] + radius):
        for y in range(center[1] - radius, center[1] + radius):
            if (x - center[0]) ** 2 + (y - center[1]) ** 2 <= radius ** 2:
                imagem.putpixel((x, y), BLUE)

    return imagem


def bandeira_costa_do_marfim(height):
    width = 3 * height // 2
    ORANGE = (255, 165, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 128, 0)
    image = Image.new("RGB", (width, height), WHITE)

    offset = width // 3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), ORANGE)
            image.putpixel((x + 2 * offset, y), GREEN)

    return image


def bandeira_alemanha(height):
    width = 3 * height // 2
    BLACK = (0, 0, 0)
    RED = (204, 0, 0)
    GOLD = (255, 204, 0)
    image = Image.new("RGB", (width, height), BLACK)

    offset = height // 3
    for y in range(offset):
        for x in range(width):
            image.putpixel((x, y), BLACK)
            image.putpixel((x, y + offset), RED)
            image.putpixel((x, y + 2 * offset), GOLD)

    return image


def bandeira_inglaterra(height):
    width = 3 * height // 2
    WHITE = (255, 255, 255)
    RED = (204, 0, 0)
    image = Image.new("RGB", (width, height), WHITE)

    cross_width = height // 8  
    cross_offset = (height - cross_width) // 2 

    for x in range(width):
        for y in range(cross_offset, cross_offset + cross_width):
            image.putpixel((x, y), RED)

    stripe_width = cross_width
    stripe_offset = (width - stripe_width) // 2  
    for x in range(stripe_offset, stripe_offset + stripe_width):
        for y in range(height):
            image.putpixel((x, y), RED)

    return image


def bandeira_franca(height):
    width = 3 * height // 2
    BLUE = (0, 85, 164)
    WHITE = (255, 255, 255)
    RED = (239, 65, 53)
    image = Image.new("RGB", (width, height), WHITE)

    offset = width // 3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2 * offset, y), RED)

    return image


def bandeira_japao(height):
    width = 3 * height // 2
    WHITE = (255, 255, 255)
    RED = (173, 35, 51)

    r = 3 * height // 10
    c = (width // 2, height // 2)
    image = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(image)
    draw.ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), fill=RED)

    return image

def bandeira_holanda(height):
    width = 3 * height // 2
    RED = (174, 28, 40)
    BLUE = (33, 70, 139)
    WHITE = (255, 255, 255)
    image = Image.new("RGB", (width, height), RED)

    offset = height // 3
    for y in range(offset):
        for x in range(width):
            image.putpixel((x, y), RED)
            image.putpixel((x, y + offset), WHITE)
            image.putpixel((x, y + 2 * offset), BLUE)

    return image

def bandeira_polonia(height):
    width = 3 * height // 2
    WHITE = (255, 255, 255)
    RED = (220, 20, 60)  
    image = Image.new("RGB", (width, height), WHITE)  
    
    offset = height // 2
    for x in range(image.width):
        for y in range(offset):
            image.putpixel((x, y), WHITE)
    for x in range(image.width):
        for y in range(offset, height):
            image.putpixel((x, y), RED)
    
    return image

def bandeira_suica(height):
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    image = Image.new("RGB", (height, height), RED) 
    
    cross_width = height // 6
    cross_length = height // 2
    
    left = (image.width - cross_width) // 2
    top = (image.height - cross_length) // 2
    right = left + cross_width
    bottom = top + cross_length
    
    draw = ImageDraw.Draw(image)
    draw.rectangle([left, top, right, bottom], fill=WHITE)  
    draw.rectangle([top, left, bottom, right], fill=WHITE)  
    
    return image

def bandeira_belgica(height):
    width = 3 * height // 2
    BLACK = (0, 0, 0)
    RED = (206, 17, 38)
    YELLOW = (255, 255, 0)
    image = Image.new("RGB", (width, height), YELLOW)

    offset = width // 3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), BLACK)
            image.putpixel((x + 2 * offset, y), RED)

    return image


def bandeira_peru(height):
    width = 3 * height // 2
    WHITE = (255, 255, 255)
    RED = (206, 17, 38)
    image = Image.new("RGB", (width, height), WHITE)

    offset = width // 3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), RED)
            image.putpixel((x + 2 * offset, y), RED)

    return image


def bandeira_nigeria(height):
    width = 3 * height // 2
    WHITE = (255, 255, 255)
    GREEN = (0, 135, 81)
    image = Image.new("RGB", (width, height), WHITE)

    offset = width // 3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), GREEN)
            image.putpixel((x + 2 * offset, y), GREEN)

    return image

def bandeira_estonia(height):
    width = 3 * height // 2
    BLACK = (0, 0, 0)
    BLUE = (0, 161, 222)
    WHITE = (255, 255, 255)
    image = Image.new("RGB", (width, height), BLUE)

    offset = height // 3
    for y in range(offset):
        for x in range(width):
            image.putpixel((x, y), BLUE)
            image.putpixel((x, y + offset), BLACK)
            image.putpixel((x, y + 2 * offset), WHITE)

    return image

def bandeira_emirados_arabes(height):
    width = 3 * height // 2
    GREEN = (0, 122, 61)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (206, 17, 38)
    
    image = Image.new("RGB", (width, height), WHITE)  
    draw = ImageDraw.Draw(image)

    offset = height // 3
    for y in range(offset):
        for x in range(width):
            image.putpixel((x, y), GREEN)
            image.putpixel((x, y + offset), WHITE)
            image.putpixel((x, y + 2 * offset), BLACK)

    vertical_stripe_width = width // 5  
    draw.rectangle([0, 0, vertical_stripe_width, height], fill=RED)  

    return image

def bandeira_argentina(height):
    width = 3 * height // 2
    BLUE = (109, 167, 192)  
    WHITE = (255, 255, 255)  
    YELLOW = (255, 255, 0)  

    image = Image.new("RGB", (width, height), BLUE)
    draw = ImageDraw.Draw(image)

    offset = height // 3
    for y in range(offset):
        for x in range(width):
            image.putpixel((x, y), BLUE)
            image.putpixel((x, y + offset), WHITE)
            image.putpixel((x, y + 2 * offset), BLUE)

    circle_radius = height // 8
    circle_center = (width // 2, height // 2)
    draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                  circle_center[0] + circle_radius, circle_center[1] + circle_radius),
                 fill=YELLOW)

    return image

def bandeira_bangladesh(height):
    width = 3 * height // 2
    GREEN = (0, 128, 0)  # Verde
    RED = (206, 17, 38)  # Vermelho

    image = Image.new("RGB", (width, height), GREEN)
    draw = ImageDraw.Draw(image)

    r = 3 * height // 10
    c = (width // 2 - height // 5, height // 2)  
    draw = ImageDraw.Draw(image)

    draw.ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), fill=RED)

    return image

def bandeira_portugal(height):
    width = 3 * height // 2
    GREEN = (0, 128, 0)
    RED = (206, 17, 38)
    YELLOW = (255, 255, 0)
    
    image = Image.new("RGB", (width, height), GREEN)
    draw = ImageDraw.Draw(image)
    
    green_width = int(0.4 * width)
    
    draw.rectangle([0, 0, green_width, height], fill=GREEN)
    draw.rectangle([green_width, 0, width, height], fill=RED)
    
    radius = height // 4.5
    
    center = (green_width, height // 2)
    
    draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=YELLOW)
    
    return image

def bandeira_austria(height):
    width = 3 * height // 2
    RED = (174, 28, 40)
    WHITE = (255, 255, 255)
    image = Image.new("RGB", (width, height), RED)

    offset = height // 3
    for y in range(offset):
        for x in range(width):
            image.putpixel((x, y), RED)
            image.putpixel((x, y + offset), WHITE)
            image.putpixel((x, y + 2 * offset), RED)

    return image



if __name__ == "__main__":
    height = 700
    bandeiras = [bandeira_italia(height), bandeira_brasil(height), bandeira_costa_do_marfim(height), bandeira_alemanha(height), bandeira_inglaterra(height), bandeira_franca(height), bandeira_japao(height), bandeira_holanda(height), bandeira_polonia(height), bandeira_suica(height), bandeira_belgica(height), bandeira_peru(height), bandeira_nigeria(height), bandeira_estonia(height), bandeira_emirados_arabes(height), bandeira_argentina(height), bandeira_bangladesh(height), bandeira_portugal(height), bandeira_austria(height)]
    
    margin = 75

    max_per_row = 6
    num_rows = (len(bandeiras) + max_per_row - 1) // max_per_row  # Número de linhas necessárias
    combined_width = (bandeiras[0].width + margin) * max_per_row  # Largura total considerando a margem
    max_height = (bandeiras[0].height + margin) * num_rows  # Altura total
    combined_image = Image.new("RGB", (combined_width, max_height), (200, 200, 200))
    
    draw_x = 0
    draw_y = 0

    for index, bandeira in enumerate(bandeiras):
        combined_image.paste(bandeira, (draw_x, draw_y))
        draw_x += bandeira.width + margin
        if (index + 1) % max_per_row == 0:  # Se exceder o número máximo por linha, vá para a próxima linha
            draw_x = 0
            draw_y += bandeira.height + margin
    
    combined_image.show()