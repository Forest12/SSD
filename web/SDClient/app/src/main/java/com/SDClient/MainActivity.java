package com.SDClient;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import com.bumptech.glide.Glide;

import java.net.URISyntaxException;

import io.socket.client.IO;
import io.socket.client.Socket;
import io.socket.emitter.Emitter;


public class MainActivity extends AppCompatActivity {
    private Socket mSocket;
    private String imageUrl = "";
    private Context mContext;
    private ImageView video;
    {
        try {
            mSocket = IO.socket("http://192.168.31.55:3000");
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = this;
        video = (ImageView) findViewById(R.id.video);

        mSocket.connect();
        mSocket.on("Image",image);

        Button send = (Button)findViewById(R.id.button);
        send.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                mSocket.emit("moblie","start");
            }
        });
    }

    private Emitter.Listener image = new Emitter.Listener() {
        @Override
        public void call(final Object... args) {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    String receivedData = (String) args[0];
                    imageUrl = receivedData;
                    Glide.with(mContext).load(imageUrl).into(video);
                }
            });
        }
    };
}
