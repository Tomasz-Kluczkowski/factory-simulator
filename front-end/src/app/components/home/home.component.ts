import {Component, OnInit} from '@angular/core';
import {FactoryConfigService} from '../../services/factory-config/factory-config.service';
import {FactoryConfigAPIResource, FactoryConfigAPIResponse} from '../../models/factory-config.models';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  factoryConfigs: FactoryConfigAPIResource[];

  constructor(private factoryConfigService: FactoryConfigService) { }

  ngOnInit(): void {
  }

  onGetConfigsClicked() {
    this.factoryConfigService.list().subscribe(
      (data) => {
        this.factoryConfigs = data;
      }
    );
  }
}
