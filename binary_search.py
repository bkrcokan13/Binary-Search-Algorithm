



class BinarySearch():
    def InterativeAlgorithm(self,numArr, target, start, end):

        if start > end:
            return -1


        # Calculate search mid index
        calculateMid =  (start + end) // 2

        # Get mid value
        midValue = numArr[calculateMid]

        if  midValue == target:
            return calculateMid
        elif midValue > target:
            # Focus left side
            return  self.InterativeAlgorithm(numArr, target, start, calculateMid -1)
        else:
            return self.InterativeAlgorithm(numArr, target, calculateMid + 1, end)
    
    def StartApp(self):
        numberList = [2,4,6,8,10,12,14,16,18,20,22,24]

        targetNumber = 18

        resultSearch = self.InterativeAlgorithm(numberList, targetNumber, 0, len(numberList) -1)

        if resultSearch != -1:
            print(f"Target number ({targetNumber}) founded index ({resultSearch})")
        else:
            print(f"Target number ({targetNumber}) is not found !")


app = BinarySearch()
app.StartApp()