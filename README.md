# SensorServer
移动端与Flask服务端通信
移动端采用OKHttp的服务来进行Post请求  

``` Java
mSubmitBtn.setOnClickListener(new View.OnClickListener() {
//点击提交按钮后进行POST的构造
            @Override
            public void onClick(View v) {
                String light = mLightEt.getText().toString();
                String temp = mTempEt.getText().toString();
                String magnetic = mMagicEt.getText().toString();

                Log.i("1",light+"--"+temp+"--"+magnetic);
                //SendMessage(light,temp,magnetic,"http://127.0.0.1:5000/demo");
                SendTask sendTask = new SendTask();
                sendTask.execute(light,temp,magnetic);

            }
        });
```  
``` Java
    private class SendTask extends AsyncTask<String, Void, Integer> {
        private String response_message;
        private int ret_code;
        @Override
        protected Integer doInBackground(String... strings) {
            String light = strings[0];
            String temp = strings[1];
            String magnetic = strings[2];
            String url = "http://192.168.0.106:5000/demo";
            //String url = MyContract.SERVER_URL + "register";
            OkHttpClient client = new OkHttpClient();
            RequestBody requestBody = new FormBody.Builder()
                    .add("light", light)
                    .add("temp", temp)
                    .add("magnetic",magnetic)
                    .build();
            Request request = new Request.Builder()
                    .url(url)
                    .post(requestBody)
                    .build();

            try {
                Response response = client.newCall(request).execute();
                response_message = response.body().string();
            } catch (IOException e) {
                e.printStackTrace();
                return 1;
            }

            return 1;
        }
    }
   
