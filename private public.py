private クラス外から参照や変更できない
public　クラス外から参照や変更できない
class ctest2{
  public static void main(String args[]){
    Television tv1 = new Television();
# できない
    tv1.channelNo = 1;
  }
}

class Television{
  private int channelNo;

  void setChannel(int newChannelNo){
    channelNo = newChannelNo;
    System.out.println("新しいChannelNo=" + channelNo);
  }
}
class ctest3{
  public static void main(String args[]){
    Television tv1 = new Television();

    tv1.setChannel(1); #クラス内のメソッド経由で変更するのでできる
  }
}

class Television{
  private int channelNo;

  void setChannel(int newChannelNo){
    channelNo = newChannelNo;
    System.out.println("新しいChannelNo=" + channelNo);
  }
}
publicは省略することが出来るので、単に下記のように記述も出来る。

変数の型 メンバ変数名;
