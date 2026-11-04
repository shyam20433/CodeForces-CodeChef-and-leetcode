class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i]=image[i][::-1]
        for row in image:
            for i in range(len(row)):
                if row[i]==1:
                    row[i]=0
                else:
                    row[i]=1
        return image