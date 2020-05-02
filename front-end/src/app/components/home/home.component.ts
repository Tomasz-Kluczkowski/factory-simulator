import {Component, OnInit} from '@angular/core';
import {FactoryConfigService} from '../../services/factory-config/factory-config.service';
import {FactoryConfigAPIResponse} from '../../models/factory-config.models';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  factoryConfigs: FactoryConfigAPIResponse[];

  constructor(private factoryConfigService: FactoryConfigService) { }

  ngOnInit(): void {
  }

  onGetConfigsClicked() {
    this.factoryConfigService.getAllFactoryConfigs().subscribe(
      (data) => {
        console.log(data);
        this.factoryConfigs = data;
      }
    );
  }
}
