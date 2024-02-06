import base64 as b64

texto = "Vm0wd2QyUXlWa2hWV0doVllteEtWMVl3WkRSWFJteFZVbTVrVmxKc2NIcFhhMk0xVmpGS2RHVkdXbFpOYm1oUVdWZDRTMk14VG5OWGJHUlRUVEZLVVZkV1kzaFRNVWw0V2toR1VtSlZXbFJXYWtwdlpWWmFkR05GU214U2JWSkpWbTEwYzJGV1NuUlZiR2hoVmpOb2FGWldXbUZqYkhCSlkwZDRVMkpXU2xsV1Z6QXhVekpHUjFOdVVtaFNlbXhXVm0weGIxSkdjRmRYYlhSWFRWWndlbFl5TVRSVk1rcFhVMnhzVjFaNlFYaFdSRXBIVWpGT2RWUnNhR2hsYlhoWlYxZDRiMVV3TUhoV1dHaFlZbGhTV0ZSV2FFTlRiR3QzV2tSU1ZrMUVSa1pXYlhCaFZqQXhkVlZ1V2xaaGExcGhXbFphVDJOdFNrZFRiV3hvWld4YWIxWnRNVEJXYXpGWFUydGtXRmRIYUZsWmEyaERZekZhYzFWclpGUmlSM2hYVmpKNGExWlhTa2RqUmxwWFlsaFNlbFpxUm1GU2JVVjZZVVprYUdFelFrbFdiWEJIVkRKU1YxZHVUbFJpVjNoVVZGY3hiMkl4V25STlJFWnJUVlZ3ZVZSV1ZtdGhiRXAwWVVoT1ZtRnJOVlJXTVZwaFkxWkdWVkpzVGs1WFJVcElWbXBLTkdFeFdsaFRiRnBxVWxkU1lWbFhjekZqYkZweFVtMUdVMkpWVmpaWlZWcHJWakZLVjJOSE9WaGhNVnBvVmtSS1RtVldUbkpoUjJoVFlrVndWVlp0TURGUk1rbDRWMWhvV0dKRk5WUlVWbFY0VGxaYWRFNVZPVmRpVlhCSVdUQmFjMWR0U2toaFJsSmFUVlp3VkZacVJuZFNWbEp5VGxkc1UySkhPVE5XYTFwaFZURlZlVkpyWkZoaWEzQndWV3RhZDFsV1duTlhibVJPVFZac00xWXlNVWRWTWtwR1RsUkdWazF1YUZoWlZWVjRZekZPY21KR2FGZFNXRUV5VjJ4V1lWbFdXWGhqUld4VllrWktjRlZxUmt0V1ZscEhWV3RLYTAxRVJsTlZSbEYzVUZFOVBRPT0="

def descifrartexto(texto):
  b64.b64decode(texto)
  #b64.b64encode(input("Ingrese el texto a codificar: "))

def desc_img(img):
  image = open('deer.gif', 'rb')
  image_read = image.read()
  image_64_encode = b64.encodestring(image_read)
  image_64_decode = b64.decodestring(image_64_encode) 
  image_result = open('deer_decode.gif', 'wb') # create a writable image and write the decoding result
  image_result.write(image_64_decode)
  image_result.close()
  return image_result

if __name__ == '__main__':
  for i in range(8):
    result_img = desc_img(flag.png)
    print(result_img)
    resultado_letra = descifrartexto(texto)
    print(resultado_letra)

