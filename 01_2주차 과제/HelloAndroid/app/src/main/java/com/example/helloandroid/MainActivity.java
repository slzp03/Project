package com.example.helloandroid;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button button1,button2,button3,button4;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        getSupportActionBar().setDisplayShowHomeEnabled(true);
        getSupportActionBar().setIcon(R.drawable.icon);
        // 액션바에 아이콘 삽입 기능

        button1=(Button)findViewById(R.id.button1); //뷰에서 id가 button1인 것을 변수 button1로 사용
        button2=(Button)findViewById(R.id.button2); //뷰에서 id가 button2인 것을 변수 button2로 사용
        button3=(Button)findViewById(R.id.button3); //뷰에서 id가 button3인 것을 변수 button3로 사용
        button4=(Button)findViewById(R.id.button4); //뷰에서 id가 button4인 것을 변수 button4로 사용

        button1.setOnClickListener(new View.OnClickListener() {   //button1을 클릭하면 실행
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"홈페이지를 엽니다.",Toast.LENGTH_SHORT).show();
                //토스트 메세지로 "홈페이지를 엽니다." 출력
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://m.nate.com"));
                //인텐트를 생성하여 Uri 전송
                startActivity(intent);
                //인텐트 실행

            }
        });

        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"전화를 겁니다.",Toast.LENGTH_SHORT).show();
                //토스트 메세지로 "전화를 겁니다." 출력
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("tel:911"));
                //인텐트를 생성하여 Uri 전송
                startActivity(intent);
                //인텐트 실행
            }
        });

        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"갤러리를 엽니다.",Toast.LENGTH_SHORT).show();
                //토스트 메세지로 "갤러리를 엽니다." 출력
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("content://media/internal/images/media"));
                //인텐트를 생성하여 Uri 전송
                startActivity(intent);
                //인텐트 실행

            }
        });

        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"프로그램을 종료합니다.",Toast.LENGTH_SHORT).show();
                //토스트 메세지로 "프로그램을 종료합니다." 출력
                finish();
                //프로그램 종료
            }
        });
    }
}
