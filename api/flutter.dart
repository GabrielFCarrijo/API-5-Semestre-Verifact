import 'package:http/http.dart' as http;
import 'dart:convert';

void sendPredictionRequest(String inputData) async {
  final url = 'NGROK_PUBLIC_URL/predict'; // substitua pela URL pública do ngrok
  final response = await http.post(
    Uri.parse(url),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'input': inputData}),
  );

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    print('Prediction: ${data['prediction']}');
  } else {
    print('Error: ${response.body}');
  }
}
