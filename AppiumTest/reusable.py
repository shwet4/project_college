from xml.dom import minidom


def read_tag(tag):
    file_xml=minidom.parse('C:/Users/158260/PycharmProjects/testscript/AppiumTest/testdata.xml')
    data=file_xml.getElementsByTagName(tag)[0]

    return data.firstChild.data
# def read_csv(filename):
#     data=[]
#
#     csvdata=open(filename,"r")
#
#     reader=csv.reader(csvdata)
#     next(reader)
#     for r in reader:
#         data.append(r)
#     return data


