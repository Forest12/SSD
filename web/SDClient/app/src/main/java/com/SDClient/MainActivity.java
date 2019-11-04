package com.SDClient;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;

import com.bumptech.glide.Glide;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.iid.InstanceIdResult;

import java.net.URISyntaxException;

import io.socket.client.IO;
import io.socket.client.Socket;
import io.socket.emitter.Emitter;


public class MainActivity extends AppCompatActivity {
    private String token;
    private Socket mSocket;
    private String imageUrl = "";
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
        video = (ImageView) findViewById(R.id.video);

        mSocket.connect();
        mSocket.on("Image",image);


        ImageButton send = (ImageButton)findViewById(R.id.setting);
        send.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                mSocket.emit("Token",token);
            }
        });

        FirebaseInstanceId.getInstance().getInstanceId()
                .addOnCompleteListener(new OnCompleteListener<InstanceIdResult>() {
                    @Override
                    public void onComplete(@NonNull Task<InstanceIdResult> task) {
                        token = task.getResult().getToken();
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
                    Glide.with(MainActivity.this).load(imageUrl).into(video);
                }
            });
        }
    };

}
