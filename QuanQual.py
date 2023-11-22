class QuanQual():
    def QuanQual(dataset):
        Quan=[]
        Qual=[]
        for columnName in dataset.columns:
            print ("columnNmae")
            if(dataset[columnName].dtypes=="O"):
                print("Quan")
                Quan.append(columnName)
            else:
                print("Qual")
                Qual.append(columnName)
        return Quan,Qual

