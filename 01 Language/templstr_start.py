# demonstrate template string functions

from string import Template

def main():
    # Usual string formatting with format()
    str1 = "I am learning {0}".format("Python")
    print(str1)
    
    # TODO: create a template with placeholders
    templ = Template("I am leaning ${title}")
    
    # TODO: use the substitute method with keyword arguments
    str2 = templ.substitute(title = "Python")
    print(str2)
    
    # TODO: use the substitute method with a dictionary
    data = {
        "title": "Python"
    }
    str3=templ.substitute(data)
    print(str3)

    
if __name__ == "__main__":
    main()
    