package com.runapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;
import android.widget.Button;



public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button freeRun;
    private Button recommendedRun;
    private Button playMusic;
    private View view1;
    private View view2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        freeRun = (Button)findViewById(R.id.button2);
        recommendedRun = (Button)findViewById(R.id.button3);

        view1 = findViewById(R.id.mapView);


    }
    @Override
    public void onClick(View v){
        switch (v.getId()){
            case R.id.button2:
                Log.d("MainActivity","테스트중");
                view1.setVisibility(View.VISIBLE);
                view1.setVisibility(View.GONE);

        }


    }
}
